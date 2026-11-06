# Auditoría v4: informe (18 págs.)

**Fecha:** 5-nov-2026. Reemplaza a la v3.

**Qué se revisó:**
- El texto completo del PDF, comparado palabra por palabra con la versión auditada en la v3.
- El registro de compilación de LaTeX.
- Los requisitos de la guía y la rúbrica.

---

## 1. Cambios desde la v3

| # | Cambio | Verificación |
|---|---|---|
| R1 | §6.2: "quedan sobre ella" → "quedan **por encima de la teórica**" | ✅ Aplicado; ningún otro texto cambió |
| R2 | Cuadro 7, fila del convexo: "No se forma" → "**No se formó** en la pantalla" | ✅ Aplicado |

## 2. Hallazgos técnicos nuevos (corregidos en esta revisión)

| # | Hallazgo | Corrección |
|---|---|---|
| T1 | Advertencia de `fancyhdr`: la altura del encabezado era de 12 pt. Quedaba muy justo, pero no se veía como error. | Se fijó `\headheight` en 14 pt. |
| T2 | La ecuación del ejemplo de cálculo d_o > R (§4.4) se salía 0.7 pt del margen. | Se separó en dos líneas: d_i y M en una, la diferencia porcentual en otra. |

**Compilación actual:** 0 errores, 0 desbordes, 0 referencias sin resolver, 0 advertencias de encabezado.

## 3. Estado de los requisitos

| Área | Estado |
|---|---|
| Cálculos (todos recalculados en la v3; los números no cambiaron) | ✅ Sin errores |
| Rúbrica: 14 criterios | ✅ Todos con evidencia |
| Riesgo de descuento por resultados no obtenidos (−2) | ✅ Sin riesgo |
| Riesgo de descuento por alteración de datos (−5) | ✅ Sin riesgo |
| Requisitos de la guía (hojas firmadas, d_o = f, ≥ 6 mediciones, fotos, convexo) | ✅ |
| Coherencia con `guion_video.md` | ✅ (sin cambios de números ni de numeración) |
| **Enlace al video de YouTube** | ❌ Pendiente |
| **Enlace a los datos experimentales** | ❌ Pendiente |
| **Recuadro rojo de pendientes** | ❌ Borrar al entregar |

---

**Conclusión:** no quedan hallazgos abiertos en el contenido ni en la maquetación. Lo único que falta son los dos enlaces y el borrado del recuadro rojo.
