# Fuentes oficiales de la skill

Consultadas el **2026-10-29**. Las leyes se bajaron del sitio de la Cámara de Diputados (texto vigente que publica la
propia Cámara) y se leyeron artículo por artículo; el catálogo y las páginas son del SAT. Ninguna regla de la skill sale
de un blog, de un proveedor de facturación ni de memoria. **Una ley cambia:** antes de usar la skill en un año distinto,
compara la fecha de «última reforma» de F1–F3 con la que aparece hoy en la misma liga.

| ID | Documento | URL | Versión consultada | Lo que la skill toma de ahí |
|---|---|---|---|---|
| F1 | Ley del Impuesto sobre la Renta (LISR) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | Texto vigente, última reforma DOF 01-04-2024 | Art. 100 (actividad empresarial y servicios profesionales, «honorarios»); art. 103 (qué deduce esa persona física y remisión al art. 28); art. 104 (inversiones por porcentaje); art. 105 fr. I, II, IV, VI y VIII (efectivamente erogado y pagado en el periodo que corresponda — fr. I; estrictamente indispensable — fr. II; restadas una sola vez — fr. IV; comprobante a más tardar el día de la anual y con fecha del ejercicio, y remisión al art. 27 fr. III — fr. VI y VIII); art. 27 fr. III (comprobante fiscal; pagos de más de $2,000.00 por transferencia, cheque nominativo, tarjeta o monedero; combustible siempre por esos medios y con el permiso del proveedor en el comprobante); art. 28 fr. III, IV, V, VI y XX (obsequios, representación, viáticos y sus topes, sanciones, 91.5 % de restaurantes y bares); art. 36 fr. II (inversión en automóviles: $175,000.00 en el supuesto general y $250,000.00 para los vehículos eléctricos, híbridos y de hidrógeno descritos en esa fracción, con excepción para ciertos arrendadores); art. 113-E y 113-F (RESICO de personas físicas: paga sobre ingresos cobrados «sin aplicar deducción alguna») |
| F2 | Ley del Impuesto al Valor Agregado (LIVA) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | Texto vigente, última reforma DOF 12-11-2021 | Art. 5o. fr. I (IVA acreditable solo de lo estrictamente indispensable, que es lo deducible para ISR «aun cuando no se esté obligado al pago de este último»; lo parcialmente deducible acredita en la misma proporción); fr. II (IVA trasladado expresamente y por separado en el comprobante); fr. III (efectivamente pagado en el mes); fr. IV (IVA retenido y enterado) |
| F3 | Código Fiscal de la Federación (CFF) | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | Texto vigente, última reforma DOF 09-04-2026 | Art. 29-A fr. IV (RFC, nombre, código postal y uso del CFDI del receptor); fr. VII a) y b) (pago en una exhibición o comprobante por cada pago posterior que señale el folio del comprobante original); fr. VII c) (forma de pago) |
| F4 | SAT — Catálogos del CFDI 4.0 (`catCFDI_V_4_20261015.xls`), enlazado desde la página del Anexo 20 | http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_20261015.xls | Archivo del 2026-10-15 (guardado por el SAT el 2026-10-13) | `c_UsoCFDI` (G01–G03, I01–I08, D01–D10, S01, CP01, CN01), `c_FormaPago` (01 efectivo … 99 por definir), `c_MetodoPago` (PUE, PPD), `c_TipoDeComprobante` (I, E, T, N, P), `c_RegimenFiscal` (612, 626…), `c_ObjetoImp` y las claves de producto del ejemplo (15101514 gasolina, 90101501 restaurantes, 43211503 computadoras portátiles…) |
| F5 | SAT — Formato de factura (Anexo 20) | https://wwwmatnp.sat.gob.mx/consultas/35025/formato-de-factura-electronica-(anexo-20) | Página vista el 2026-10-29 | CFDI 4.0 es la única versión válida desde el 1 de abril de 2023; nombre, régimen fiscal y domicilio fiscal del receptor son obligatorios |
| F6 | SAT — Complemento de pagos | https://wwwmatnp.sat.gob.mx/consultas/92764/comprobante-de-recepcion-de-pagos | Página vista el 2026-10-29 (cita la regla 2.7.1.32 de la RMF para 2024 como fundamento) | Los pagos diferidos o en parcialidades (PPD) se amparan con un comprobante de pago (tipo P, versión 2.0 obligatoria desde el 1 de abril de 2023) |
| F7 | SAT — Consulta y recuperación de comprobantes (descarga masiva) | https://wwwmat.sat.gob.mx/cs/Satellite?c=ConsultaInfo&childpagename=SatTyR%2FConsultaInfo%2FSAT_LandingConsultaInformacion&cid=1462231542968&packedargs=d%3DTouch&pagename=TySWrapper | Página vista el 2026-10-29 | Entrada con e.firma o contraseña; hasta 2,000 XML por día; el portal muestra los primeros 500 por consulta |
| F8 | SAT — Verifica tus facturas | https://wwwmat.sat.gob.mx/aplicacion/80523/verifica-tus-facturas-electronicas | Página vista el 2026-10-29 | Verificar un CFDI no requiere entrar con contraseña: folio fiscal y RFC de emisor y receptor |
| F9 | SAT — Datos abiertos, contribuyentes publicados (art. 69-B) | https://www.sat.gob.mx/minisitio/DatosAbiertos/contribuyentes_publicados.html | Página vista el 2026-10-29; decía «actualizada al 30 de septiembre de 2026» en la sección 69-B | Listado de presuntos, definitivos, desvirtuados y sentencias favorables, para que el usuario busque a sus proveedores |
| F10 | Ley Federal del Derecho de Autor (LFDA) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFDA.pdf | Texto vigente, última reforma DOF 14-05-2026; consulta 2026-10-29 | Arts. 18–21 (derechos morales) y 24–27 (derechos patrimoniales y autorización de uso): la obra se usa según la autorización de su autor. Las condiciones comerciales concretas de este paquete son las del LICENSE de Heroldo, no una transcripción de la ley; esta referencia no es asesoría jurídica |

## Lo que la skill NO afirma, y por qué

- **No dictamina deducibilidad.** El art. 105 fr. II de F1 pide que el gasto sea «estrictamente indispensable»: eso
  depende del giro y lo decide el contador. La skill marca la duda (bandera B11) y nunca escribe «deducible» ni
  «no deducible» como veredicto.
- **No consulta al SAT.** Leer un XML no prueba que esté vigente ni que el emisor no esté en el 69-B. El usuario lo
  consulta con F8 y F9; la skill le da la lista de UUID y RFC para copiar.
- **No cita números de regla de la RMF como propios.** La Resolución Miscelánea Fiscal cambia cada año y renumera.
  Donde el SAT la cita (F6), la skill repite la cita con su año; todas las banderas se sostienen en la ley (F1–F3).
- **No calcula impuestos ni declaraciones.** Los totales de IVA son lo que dice cada XML; el IVA acreditable final,
  los pagos provisionales, la depreciación de inversiones y las deducciones personales los calcula el contador.

## Reglas propias del paquete (no son del SAT)

El empate entre el Excel y los XML (UUID; si no hay, total con diferencia máxima de $1.00 y el mismo proveedor), la
lista de categorías, el orden del reporte, el nombre de las banderas y el correo son decisiones de diseño de esta skill.
No son obligaciones fiscales.
