# Casos límite (se cuentan a mano)

Nueve situaciones que el ejemplo principal no cubre. Cada una dice la entrada mínima (los campos del XML que importan),
lo que la skill debe hacer y el número que debe salir. Todo es FICTICIO de Andén Norte; los UUID terminan en `…09xx`
solo para leerlos rápido.

## 1 · RESICO persona física (régimen 626)

**Entrada:** receptor con `RegimenFiscalReceptor="626"`. Dos CFDI: laptop (uso I04, PUE, forma 04; $15,000.00 + IVA
$2,400.00 = $17,400.00) y restaurante (clave 90101501, PUE, forma 04; $1,000.00 + IVA $160.00 = $1,160.00).

**Debe salir:**
- Bajo la línea de alcance, la línea fija de RESICO (ISR sin deducción alguna, LISR arts. 113-E y 113-F; el reporte
  sirve para el IVA, LIVA art. 5o. fr. I).
- Laptop: **sin banderas** (B09 no se marca en RESICO), categoría Inversiones.
- Restaurante: B08 con «referencia 8.5 %: $85.00».
- Resumen: 1 sin banderas $17,400.00 · 1 por revisar $1,160.00 · total con CFDI $18,560.00; IVA $2,560.00.

## 2 · Factura a crédito (PPD) con su comprobante de pago

**Entrada:** mes del reporte: **septiembre de 2026**. CFDI I de papelería, `MetodoPago="PPD"`, `FormaPago="99"`,
UUID …0921, `Moneda="MXN"`, $5,000.00 + IVA $800.00 = $5,800.00. Más un CFDI tipo P del mismo proveedor cuyo
`DoctoRelacionado IdDocumento` es …0921 con `Moneda="MXN"` (la del documento relacionado), `FechaPago="2026-09-18T12:00:00"`,
`ImpPagado="5800.00"`, `ImpSaldoAnt="5800.00"` e `ImpSaldoInsoluto="0.00"`. Todo FICTICIO de Andén Norte.

**Debe salir:**
- La factura …0921 **sin B06 porque documenta pago completo en septiembre, sin afirmar IVA acreditable** (el Paso 4
  quita B06 solo con pago completo y `FechaPago` del mes del reporte).
- El tipo P va a «Fuera del reporte»: «comprobante de pago de la factura …0921; no es un gasto nuevo».
- Total con CFDI **$5,800.00**, no $11,600.00 (el pago no se suma dos veces).

**Variante · el mismo pago completo, pero en octubre:** mismo par de comprobantes, con `FechaPago="2026-10-06T12:00:00"`,
`ImpPagado="5800.00"`, `ImpSaldoAnt="5800.00"`, `ImpSaldoInsoluto="0.00"`, y el reporte sigue siendo de septiembre de
2026. **Debe salir:** la factura …0921 **conserva B06** con la observación para el contador, indicando el importe y la
fecha documentados: pago completo de $5,800.00 el 06/10/2026, fuera del mes del reporte. El tipo P sigue yendo «Fuera
del reporte» y el total con CFDI sigue siendo **$5,800.00**: la diferencia con el caso de arriba es solo la `FechaPago`.

## 3 · Nota de crédito (egreso)

**Entrada:** CFDI I de mercancía (uso G01, PUE, forma 03), UUID …0931, $10,000.00 + IVA $1,600.00 = $11,600.00.
CFDI tipo E del mismo proveedor, uso G02, relacionado a …0931, $1,000.00 + IVA $160.00 = $1,160.00.

**Debe salir:**
- La nota con B15: «Nota de crédito: se resta del gasto que relaciona (UUID …0931)», importes con signo negativo.
- Mercancía y materia prima: 2 comprobantes, subtotal **$9,000.00**, IVA **$1,440.00**, total **$10,440.00**.
- Si la nota no trae UUID relacionado, la misma B15 con la acción de preguntar al proveedor a qué factura corresponde,
  y se resta igual en la categoría del gasto que más se parece, diciéndolo.

## 4 · Moneda extranjera

**Entrada:** CFDI de un proveedor mexicano de software, `Moneda="USD"`, `TipoCambio="18.50"`, subtotal 100.00, IVA
16.00, total 116.00, PUE, forma 04.

**Debe salir:** B14 con «se convirtió con el tipo de cambio del propio CFDI (18.50)»; en el reporte, subtotal
**$1,850.00**, IVA **$296.00**, total **$2,146.00** (MXN). Sin `TipoCambio`, B14 con «queda pendiente» y el comprobante
no suma en pesos hasta que el contador dé el tipo de cambio; el resumen lo dice.

## 5 · Las fronteras de B01 y B04

**Entrada:** tres CFDI pagados en efectivo (forma 01), PUE, uso G03:
- A: total **$2,000.00**, a tu RFC.
- B: total **$2,000.01**, a tu RFC.
- C: total $850.00, pero el receptor es el RFC de tu hermano.

**Debe salir:**
- A: sin B04 (la ley dice «exceda de $2,000.00»; F1 art. 27 fr. III).
- B: B04.
- C: B01 («La factura está a nombre de otro RFC: no ampara un gasto tuyo») y su mensaje al proveedor en la sección 9.
  Con B01 no se marca ninguna otra bandera: primero hay que refacturarla a tu RFC.
- Resumen: 1 sin banderas $2,000.00 · 2 por revisar $2,850.01.

## 6 · Factura emitida en otro mes y pagada en el mes (B12 no mueve de mes)

**Entrada:** CFDI I de mercancía (uso G01, `MetodoPago="PPD"`, UUID …0941), emitido el 28/08/2026, $8,000.00 + IVA
$1,280.00 = $9,280.00. Más un CFDI tipo P del mismo proveedor cuyo `DoctoRelacionado IdDocumento` es …0941, con
`FechaPago` 05/09/2026, `ImpPagado` $9,280.00 e `ImpSaldoInsoluto` $0.00. Ambos archivos se incluyen en los gastos de
septiembre. Todo FICTICIO de Andén Norte.

**Debe salir:**
- La factura …0941 **se conserva** en el reporte de septiembre con B12: «Factura emitida fuera del mes del reporte
  (agosto 2026); confirmar con el contador el periodo que corresponde según el pago y el ejercicio».
- La fecha de emisión (28/08/2026) sigue visible en el detalle; nunca se expulsa automáticamente a agosto ni se mueve
  de mes por la sola fecha de la factura: el periodo fiscal lo decide el contador con la fecha y evidencia de pago.
- B06 no se marca (hay complemento que documenta pago completo en septiembre). No se calcula acreditamiento: lo decide
  el contador (LISR art. 105 fr. I, VI y VIII; LIVA art. 5o. fr. III).

## 7 · Automóvil eléctrico (B09 sin tope general impuesto)

**Entrada:** CFDI de un automóvil eléctrico (uso I04, PUE, forma 03; descripción «automóvil eléctrico»), $320,000.00 +
IVA $51,200.00 = $371,200.00. Todo FICTICIO de Andén Norte.

**Debe salir:** B09 con el añadido de automóvil («confirmar con el contador el límite aplicable; LISR art. 36 fr. II
distingue $175,000.00 en el supuesto general y $250,000.00 para los vehículos eléctricos, híbridos y de hidrógeno
descritos en esa fracción, y prevé una excepción para ciertos arrendadores»). El reporte **no** le impone el tope
general de $175,000.00: lo decide el contador.

## 8 · Vehículo sin motorización en los datos (B09 sin tope impuesto)

**Entrada:** CFDI cuya descripción solo dice «vehículo», sin ningún dato de motorización (uso I04, PUE, forma 03),
$200,000.00 + IVA $32,000.00 = $232,000.00. Todo FICTICIO de Andén Norte.

**Debe salir:** B09 con el añadido de automóvil. Sin dato de motorización **no se aplica ningún tope ni se infiere por
la palabra «vehículo»**: lo decide el contador.

## 9 · Factura PPD con pago parcial (B06 se conserva)

**Entrada:** mes del reporte: **septiembre de 2026**. CFDI I de papelería, `MetodoPago="PPD"`, `FormaPago="99"`, UUID
…0922, `Moneda="MXN"`, $5,000.00 + IVA $800.00 = $5,800.00. Más un CFDI tipo P del mismo proveedor cuyo
`DoctoRelacionado IdDocumento` es …0922 con `Moneda="MXN"` (la del documento relacionado), `FechaPago="2026-09-12T12:00:00"`,
`ImpPagado="1000.00"`, `ImpSaldoAnt="5800.00"` e `ImpSaldoInsoluto="4800.00"`. Todo FICTICIO de Andén Norte.

**Debe salir:**
- La factura …0922 **conserva B06** con el texto de pago parcial: pago documentado de $1,000.00 el 12/09/2026 (saldo
  insoluto $4,800.00); encontrar su UUID en el complemento no la deja sin observaciones. Un complemento de pago no prueba
  por sí solo el pago completo ni declara IVA acreditable.
- El tipo P va a «Fuera del reporte»: «comprobante de pago de la factura …0922; no es un gasto nuevo».
- Total con CFDI **$5,800.00**, no $6,800.00 (el pago no se suma dos veces).
