# Auditoría v2: informe, rúbrica y guion

**Fecha:** 5-nov-2026.
**Revisado:**
- `informe.pdf`, 19 páginas completas, versión actual.
- La rúbrica (Apéndice F) y los requisitos de entrega (Apéndice E).
- El borrador `guion_video.md`.

**Respecto a la auditoría v1:** esta versión la reemplaza. Verifica si los hallazgos anteriores quedaron resueltos y agrega los nuevos.

**Leyenda de tipo:**
- **A**: existe en el informe y solo hay que adaptarlo al video.
- **D**: se puede derivar de los datos o la teoría.
- **P**: lo tiene que proporcionar el grupo.

---

## 1. Seguimiento de los hallazgos de la v1

| # v1 | Hallazgo | Estado actual | Evidencia |
|---|---|---|---|
| 1.13 | Convexo: "distintas distancias" vs. "distancia arbitraria" | ✅ Resuelto | p. 5, paso 10, y p. 11, §4.5: los dos dicen "distancia arbitraria" |
| 1.9 | Caso d_o = f sin interpretar | ✅ Resuelto | p. 7, §4.1: rayos paralelos, imagen en el infinito, 1/d_i = 0 |
| 1.21 | Características del Cuadro 2 presentadas como observadas | ✅ Resuelto | p. 15, Cuadro 7: columna "Experimental", "Real (se proyectó); invertida y reducida según M"; el pie lo explica |
| — | Datos de reparto y logística | ✅ Recibidos | Integrantes 1–4, clips de los 4, animaciones en Python, cada uno graba por separado |
| 3 | Enlaces al video y a los datos | ❌ Pendiente | p. 2, "Enlaces" |
| 3 | Recuadro rojo de pendientes | ❌ Pendiente | p. 2 |

---

## 2. Informe vs. rúbrica (estado actual)

| Criterio | Pts | Evidencia (pág., sección) | Estado | Problema / acción |
|---|---|---|---|---|
| Objetivo | 0.5 | p. 2, §1.1 | Completo | — |
| Conclusión principal (intro) | 0.5 | p. 2, §1.2 | Completo | — |
| Palabras clave | 1 | p. 2, §1.3 | Completo | — |
| Equipo | 0.5 | p. 3, §3.1; Fig. 1 | Completo | — |
| Procedimiento | 2.5 | p. 4–6, §3.2; Figs. 1–4 | Completo | — |
| Tablas/gráficos | 0.5 | Cuadros 1–8, Figs. 9–12 | Completo | — |
| Tratamiento estadístico | 4 | p. 10 (§4.3), p. 12–14 (§5.1–5.4) | Completo | Valores recalculados: todos coinciden. |
| Describe resultados | 0.5 | §4–5 | Completo | — |
| Características cualitativas | 2 | p. 15, Cuadro 7; p. 11, Fig. 8 | Completo | Separa lo observado de lo deducido de M. |
| Cóncavo vs. convexo con el trazado | 1 | p. 7 (§4.1, incluye d_o = f), p. 15–17 | Completo | — |
| Interpreta el gráfico y justifica el ajuste | 3 | p. 12 (§5.1), p. 17 (§6.2) | Completo | — |
| Fuentes de error y mejoras | 1 | p. 18, §6.4, §6.6 | Completo | — |
| Conclusión (discusión) | 1 | p. 19, §7 | Completo | — |
| Reflexión adicional | 4 | §5.2, §5.4, §5.6, §6.2, §6.3, §6.7 | Completo | — |
| Descuento por cálculos (−1) | | — | Sin hallazgos | — |
| Descuento por resultados no obtenidos (−2) | | — | 1 riesgo menor | Ver N1. |
| Descuento por alteración de datos (−5) | | Cuadros 1–2 = hoja firmada | Sin hallazgos | — |

---

## 3. Hallazgos nuevos

| # | Requisito | Evidencia | Estado | Tipo | Problema | Acción |
|---|---|---|---|---|---|---|
| N1 | No presentar hipótesis como hechos | p. 18, §6.3, último párrafo: "…también dificulta colocar la pantalla y **explica** que la diferencia sea mayor que en d_o > R" | Inconsistente (menor) | — | En el caso f < d_o < R, la dificultad para colocar la pantalla es una hipótesis: la hoja no registra dónde estuvo. El resto del informe ya usa "podría" o "explicaría". | Cambiar "explica" por "podría explicar". |
| N2 | Que el documento sirva de apoyo visual | Las Figs. 1, 2, 3 y 9 y los Cuadros 5 y 8 no se citan en el texto | Parcial (estilo) | — | No afecta la rúbrica, pero sin la cita es más difícil señalar la figura en el video ("como se ve en la Figura 2…"). | Agregar una referencia breve a cada una (p. ej., "Figura 1" en §3.1 y "Figura 9" en §5.1). Opcional. |
| N3 | Enlaces obligatorios | p. 2 | Ausente | P | Sin enlaces, el documento no cumple el Apéndice E. | Al final: grabar, subir y pegar los enlaces. |

---

## 4. Borrador del guion (`guion_video.md`) vs. informe actual

El borrador se escribió antes de los pasos 1–4, así que tiene desfases que hay que corregir en el guion final (paso 6 del plan):

| # | Escena del borrador | Problema | Acción en el guion final |
|---|---|---|---|
| G1 | Escena 6: "la imagen fue real, invertida y reducida… real, invertida y ampliada" | Lo presenta como observado. El informe ahora dice que orientación y tamaño se deducen de M (riesgo de −2). | Decir "se proyectó en la pantalla, así que es real; **según la magnificación**, invertida y reducida". |
| G2 | Escena 8: "la medimos a 27.4, reducida" | Igual que G1. | "Según M, resulta reducida". |
| G3 | Escena 9: "fueron cuatro" fuentes de error | El informe tiene cinco; falta "posición de la imagen respecto de la fuente". | Incluir las cinco o decir "las principales" sin número. |
| G4 | Transiciones pensadas para grabar juntos | Ahora cada uno graba por separado. | Que cada escena abra y cierre por sí sola, con una frase de entrega o de entrada. |
| G5 | No incluye las animaciones | Ahora se quieren animaciones en Python. | Indicar en qué segundo de cada escena entra cada animación. |
| G6 | No menciona el caso d_o = f | Ahora está en §4.1. | Una frase en la escena de trazado de rayos o en la de casos. |
| G7 | Escena 1: ejemplo de la cuchara | No está en el informe; es una analogía. | Válido como gancho si se presenta como ejemplo, no como dato. Opcional: apoyarlo en las aplicaciones de §6.7.3. |
| G8 | Escena 2: espejo en 57.2 | No está confirmado, aunque coincide con la resta y con la foto de Luis. | Mantenerlo como ejemplo de la resta; no decir "estaba exactamente en 57.2". |

---

## 5. Prioridades

**Antes de escribir el guion final:**
1. **N1:** cambiar "explica" por "podría explicar" (1 palabra).
2. **Elegir las animaciones** (paso 5 del plan): define qué se muestra en cada escena.

**Durante el guion final (paso 6):**
3. Corregir G1–G6.

**Antes de entregar:**
4. **N3:** enlaces y borrar el recuadro rojo.

**Opcional:**
5. **N2:** citar en el texto las figuras y cuadros que no se citan.

---

**Conclusión:** el informe ya cubre los 22 puntos de la rúbrica sin riesgos de descuento relevantes; solo queda N1, que es una palabra. Lo pendiente está en el guion, que hay que reescribir con los cambios de los pasos 1–4, y en los enlaces de entrega.
