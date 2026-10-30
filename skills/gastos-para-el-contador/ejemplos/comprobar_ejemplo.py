#!/usr/bin/env python3
"""Comprobador OPCIONAL del ejemplo (para revisores; el usuario no lo necesita).

Repite con código las cuentas de `caso-01-septiembre-2026/salida-esperada.md`: lee los XML, quita duplicados y lo
que emitió el propio usuario, marca las banderas mecánicas de `references/banderas.md`, empata contra el CSV de gastos
y compara los totales con los esperados. Solo usa la biblioteca estándar de Python.

    python3 comprobar_ejemplo.py            sale 0 si todo cuadra con la salida esperada
"""
import csv, glob, os, sys, unicodedata
import xml.etree.ElementTree as ET
from decimal import Decimal as D

AQUI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caso-01-septiembre-2026")
YO = {"rfc": "IADR780412AN1", "cp": "64000", "reg": "612", "nombre": "ROSA IBARRA DUARTE", "mes": "2026-09"}
NS = {"cfdi": "http://www.sat.gob.mx/cfd/4", "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital"}
COMBUSTIBLE = ("15101505", "15101514", "15101515")   # diésel, gasolina regular y premium (catálogo c_ClaveProdServ)
RESTAURANTE = ("90101501",)
PERSONAL = ("501", "502", "531")                      # alimentos, bebidas y ropa: solo una pista, decide el contador


def sin_acentos(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def leer(ruta):
    r = ET.parse(ruta).getroot()
    em, rc = r.find("cfdi:Emisor", NS), r.find("cfdi:Receptor", NS)
    imp = r.find("cfdi:Impuestos", NS)
    conceptos = r.findall("cfdi:Conceptos/cfdi:Concepto", NS)
    return {
        "archivo": os.path.basename(ruta), "uuid": r.find("cfdi:Complemento/tfd:TimbreFiscalDigital", NS).get("UUID").upper(),
        "fecha": r.get("Fecha")[:10], "tipo": r.get("TipoDeComprobante"), "metodo": r.get("MetodoPago"),
        "forma": r.get("FormaPago"), "moneda": r.get("Moneda"), "sub": D(r.get("SubTotal")), "total": D(r.get("Total")),
        "iva": D(imp.get("TotalImpuestosTrasladados", "0")) if imp is not None else D(0),
        "emisor": em.get("Rfc"), "nombre": em.get("Nombre"), "rfc_r": rc.get("Rfc"), "cp_r": rc.get("DomicilioFiscalReceptor"),
        "reg_r": rc.get("RegimenFiscalReceptor"), "uso": rc.get("UsoCFDI"), "claves": [c.get("ClaveProdServ") for c in conceptos],
        "relacionados": [d.get("IdDocumento", "").upper() for d in r.iter("{http://www.sat.gob.mx/Pagos20}DoctoRelacionado")],
    }


def banderas(c, pagados):
    if c["rfc_r"] != YO["rfc"]:
        return ["B01"]                  # con B01 no se marca nada más: primero se refactura
    b = []
    if c["cp_r"] != YO["cp"] or c["reg_r"] != YO["reg"]:
        b.append("B02")
    if c["uso"] in ("S01", "CP01", "CN01") or c["uso"].startswith("D"):
        b.append("B03")
    if c["forma"] == "01" and c["total"] > D("2000.00"):
        b.append("B04")
    if c["forma"] == "01" and any(k in COMBUSTIBLE for k in c["claves"]):
        b.append("B05")
    if c["metodo"] == "PPD" and c["uuid"] not in pagados:
        b.append("B06")
    if c["metodo"] == "PUE" and c["forma"] == "99":
        b.append("B07")
    if any(k in RESTAURANTE for k in c["claves"]):
        b.append("B08")
    if c["uso"].startswith("I"):
        b.append("B09")
    if any(k.startswith(PERSONAL) for k in c["claves"]):
        b.append("B11")
    if not c["fecha"].startswith(YO["mes"]):
        b.append("B12")
    if c["moneda"] != "MXN":
        b.append("B14")
    return b


def main():
    vistos, recibidos, fuera = set(), [], []
    todos = [leer(x) for x in sorted(glob.glob(os.path.join(AQUI, "xml", "*.xml")))]
    pagados = {u for c in todos if c["tipo"] == "P" for u in c["relacionados"]}
    for c in todos:
        if c["uuid"] in vistos:
            fuera.append((c, "duplicado"))
        elif c["emisor"] == YO["rfc"]:
            fuera.append((c, "emitida por ti (ingreso)"))
        elif c["tipo"] in ("I", "E"):
            recibidos.append(c)
        else:
            fuera.append((c, f"tipo {c['tipo']}"))
        vistos.add(c["uuid"])
    for c in recibidos:
        c["b"] = banderas(c, pagados)

    filas = list(csv.DictReader(open(os.path.join(AQUI, "gastos-septiembre-2026.csv"), encoding="utf-8")))
    libres = list(recibidos)
    sin_cfdi = []
    for f in filas:
        monto = D(f["monto"])
        cand = [c for c in libres if abs(c["total"] - monto) <= D("1.00")]
        prov = sin_acentos(f["proveedor"]).split()[:1]
        cand = [c for c in cand if not prov or prov[0] in sin_acentos(c["nombre"])] or cand
        if cand:
            libres.remove(cand[0])
        else:
            sin_cfdi.append(f)

    def suma(lst, k):
        return sum((c[k] for c in lst), D(0))
    limpios = [c for c in recibidos if not c["b"]]
    revisar = [c for c in recibidos if c["b"]]
    obtenido = {
        "leidos": len(todos), "recibidos": len(recibidos), "fuera": len(fuera),
        "limpios_total": suma(limpios, "total"), "revisar_total": suma(revisar, "total"),
        "con_cfdi_sub": suma(recibidos, "sub"), "con_cfdi_iva": suma(recibidos, "iva"), "con_cfdi_total": suma(recibidos, "total"),
        "sin_cfdi_total": sum((D(f["monto"]) for f in sin_cfdi), D(0)), "sin_cfdi_n": len(sin_cfdi),
        "excel_total": sum((D(f["monto"]) for f in filas), D(0)), "xml_no_en_excel": len(libres),
        "restaurante_8_5": sum((c["sub"] * D("0.085") for c in recibidos if "B08" in c["b"]), D(0)).quantize(D("0.01")),
    }
    esperado = {
        "leidos": 11, "recibidos": 9, "fuera": 2,
        "limpios_total": D("34800.00"), "revisar_total": D("28889.00"),
        "con_cfdi_sub": D("55159.48"), "con_cfdi_iva": D("8529.52"), "con_cfdi_total": D("63689.00"),
        "sin_cfdi_total": D("4660.00"), "sin_cfdi_n": 4, "excel_total": D("68349.00"), "xml_no_en_excel": 0,
        "restaurante_8_5": D("85.00"),
    }
    banderas_esperadas = {"03-gasolina.xml": ["B05"], "04-restaurante.xml": ["B08"], "05-laptop.xml": ["B09"],
                          "06-papeleria.xml": ["B06"], "07-internet.xml": ["B02"], "08-super.xml": ["B03", "B11"],
                          "09-mostrador.xml": ["B04"]}
    malos = 0
    for k, v in esperado.items():
        ok = obtenido[k] == v
        malos += not ok
        print(f"  {'OK ' if ok else 'MAL'} {k}: {obtenido[k]} (esperado {v})")
    for c in recibidos:
        ok = c["b"] == banderas_esperadas.get(c["archivo"], [])
        malos += not ok
        print(f"  {'OK ' if ok else 'MAL'} {c['archivo']}: {c['b'] or 'sin banderas'}")
    for c, por in fuera:
        print(f"  --  {c['archivo']}: fuera del reporte ({por})")
    print(f"  --  sin CFDI: {', '.join(f['concepto'] for f in sin_cfdi)}")
    print("comprobación:", "CUADRA" if not malos else f"{malos} diferencia(s)")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
