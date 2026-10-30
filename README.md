# Gastos para el contador

Tus facturas recibidas del SAT (XML) y/o tu Excel de gastos → reporte mensual para tu contador: cada gasto
clasificado, lo que tiene factura separado de lo que no, lo que el contador debe revisar marcado con su fuente legal,
y el correo al contador y los mensajes a proveedores listos para copiar.
Para personas físicas en México: actividad empresarial, honorarios o RESICO.
**Licencia para empresa: USD 20.** Autor: Heroldo Escobedo — heroldo.org.

## Uso en 3 pasos

1. **Adjunta la skill a un chat que lea archivos:** descomprime `gastos-para-el-contador.zip` y adjunta al chat
   `SKILL.md` y los dos archivos de `references/` (`banderas.md` y `fuentes.md`); `ejemplos/` solo hace falta si le pides
   correr el ejemplo. No hay nada que instalar en tu computadora. Adjunta los archivos uno por uno. Si tu chat no
   acepta archivos `.xml` o `.csv`, abre cada uno y pega su contenido en el mensaje: la skill trabaja igual.
2. **Adjunta tus archivos:** los XML de las facturas recibidas del mes (sueltos o el ZIP tal como lo baja el SAT en
   «Consulta y recuperación de comprobantes») y/o tu Excel o CSV de gastos. Escribe:
   **«Arma mi reporte de gastos de <mes> para el contador»**. Si quieres, agrega tu régimen y el nombre y correo de
   tu contador; si no, los toma de tus facturas o deja el hueco marcado.
3. **Copia y envía:** el reporte, el correo al contador y los mensajes a proveedores salen listos. Antes de enviar,
   consulta en el SAT el estado de las facturas y la lista 69-B de tus proveedores: la skill te da la lista de folios
   y RFC para copiar y las dos ligas oficiales.

**Ruta alternativa (opcional):** instalar la skill con el conector de Agensi en claude.ai (una vez; después la pides
por su nombre) o subir `gastos-para-el-contador.zip` en Personalizar → Skills. `ejemplos/comprobar_ejemplo.py` es
opcional, para quien revise el paquete; no necesitas correrlo para usar la skill.

**Probado el 2026-10-29** con Claude, sesión nueva y sin activar nada: con los archivos adjuntos y la frase del
ejemplo, entregó el reporte completo en un solo turno, igual a la salida esperada.

## Qué recibes

- Resumen del mes con control: lo que tiene factura + lo que no = el total de tu Excel.
- Gastos por categoría (mercancía, renta, combustible, inversiones, restaurantes…).
- Comprobantes por revisar, cada uno con su bandera, la fuente legal (LISR, LIVA, CFF, catálogos del SAT, con fecha)
  y quién lo resuelve: tú con el proveedor, o tu contador.
- Gastos sin factura con qué hacer, el detalle completo para el contador y un bloque CSV para pegar en Excel.
- El correo al contador con las preguntas que solo él decide, y los mensajes para pedir refacturas, complementos de
  pago y facturas faltantes.

**No sustituye al contador ni al SAT:** pre-revisa, cruza y arma evidencia. No dice «deducible» ni «no deducible», no
calcula impuestos ni declaraciones, no consulta al SAT y no envía nada por ti. Fuera de alcance: sueldos, arrendamiento,
plataformas digitales y personas morales (la skill lo dice y entrega solo el inventario).

## Prueba sin datos propios

Escribe: **«Corre el ejemplo incluido de la skill gastos-para-el-contador»**. Si tu instalación no trae los archivos,
ábrelos del ZIP (`ejemplos/caso-01-septiembre-2026/`: los 11 XML sueltos de la carpeta `xml/` y
`gastos-septiembre-2026.csv`) y adjúntalos con la frase de `perfil.md`. Compara con `salida-esperada.md`: total del mes **$68,349.00** = $63,689.00 con factura +
$4,660.00 sin factura; 2 facturas sin banderas, 7 por revisar, 2 fuera del reporte (un duplicado y una factura que
emitió la propia usuaria). Todo es **FICTICIO de Andén Norte**: RFC, folios y nombres inventados.
`ejemplos/casos-limite.md` trae nueve casos más (RESICO, pago diferido, nota de crédito, dólares, el límite de $2,000, factura emitida en otro mes, automóvil eléctrico, motorización desconocida y pago parcial).
`ejemplos/comprobar_ejemplo.py` repite las cuentas del ejemplo con código; es opcional, para quien revise el paquete.

## Contenido

`skills/gastos-para-el-contador/SKILL.md` son las instrucciones; `references/fuentes.md`, las fuentes oficiales con
URL y fecha de consulta; `references/banderas.md`, las 16 banderas con su fuente; `ejemplos/`, entrada y salida
reproducibles;
`LICENSE`, la licencia completa. `gastos-para-el-contador.zip` lleva la carpeta
`gastos-para-el-contador/` con `SKILL.md` en su raíz, más referencias, ejemplos, README y LICENSE, para subirla sin
reorganizar nada. No depende de rutas privadas, de otras skills ni de herramientas del autor.

## Licencia

**Propiedad intelectual de Heroldo Escobedo**, con el código a la vista ([Licencia de uso de Heroldo 1.0](LICENSE)):

- **Uso personal: gratis.** Léelo, pruébalo y adáptalo para aprender o en tus propios datos.
- **Uso en una empresa o con fines de lucro: solo con compra.** Cómpralo en [Agensi](https://agensi.io/skills/gastos-para-el-contador)
  o escribe a heroldo@lolo-enterprises.com. La compra cubre a tu empresa.
- **Siempre se cita la fuente:** «Basado en una skill de Heroldo Escobedo — heroldo.org».
- No se revende ni se vuelve a publicar.

> **In English:** Source-available, not open source. Free for personal use. Business use requires purchase on
> [Agensi](https://agensi.io/skills/gastos-para-el-contador). Attribution to Heroldo Escobedo — heroldo.org is always required.
