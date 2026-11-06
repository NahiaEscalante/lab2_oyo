# Auditoría v3: informe completo (versión concisa, 18 págs.)

**Fecha:** 5-nov-2026.

**Qué se revisó:**
- El texto completo del PDF, las 18 páginas.
- La maquetación de las páginas con fórmulas y tablas largas.
- Los valores numéricos, recalculados desde la hoja firmada.
- El cumplimiento de la guía, del Apéndice E (entrega) y de la rúbrica (Apéndice F).
- La coherencia entre el informe y `guion_video.md`.

**Reemplaza a:** la auditoría v2.

---

## 1. Verificación numérica

Recalculé todos los valores a partir del Cuadro 1 y del Cuadro 2 de la hoja firmada.

| Bloque | Valores verificados | Estado |
|---|---|---|
| f_k y promedio (§4.3) | f_k de 18.95 a 19.36; f̄ = 19.18; s = 0.14; σ = 0.05; R = 38.36 ± 0.10; error 4.1 % | ✅ |
| Casos (Cuadro 2) | 33.43 / −0.743 / 0.21 %; 36.85 / −0.921 / 25.64 %; 42.43 / −1.212 / 13.36 %; −68.83 / +4.59 | ✅ (25.64 % coincide con la hoja) |
| M vs d_i (§5.1) | a = 0.0528 ± 0.0043; b = −1.09 ± 0.12; R² = 0.968; f = 18.9 ± 1.5; R = 37.8 ± 3.1; 5.4 % | ✅ |
| Inversas (§5.2) | m = −0.995 ± 0.050; b = 0.05195 ± 0.00182; R² = 0.988; f = 19.25 ± 0.67; corte horizontal 19.15; 0.1σ y 1.1σ | ✅ |
| Caso extremo (§5.4) | 6 puntos: −0.951 ± 0.070, f = 19.83 ± 0.99; reducción ~30 % | ✅ |
| Descarte d_o = R (§5.6) | 8 puntos: −1.00 ± 0.43, R² = 0.469, f = 18.8 ± 5.6; 23σ; ×8 incertidumbre | ✅ |
| Discusión | δ ≈ 1.4 cm (f → 20.00); separación 0.0017–0.0028 cm⁻¹; pendiente fija → 19.18 | ✅ |
| Reflexión | intercepto fijo → 20.1; M con distancias → 19.4 ± 0.6, R² = 0.9945 | ✅ |

**Resultado:** ningún cálculo incorrecto (sin riesgo del descuento de −1).

---

## 2. Rúbrica (Apéndice F)

| Criterio | Pts | Evidencia (pág., sección) | Estado |
|---|---|---|---|
| Objetivo | 0.5 | p. 2, §1.1 | ✅ |
| Conclusión principal | 0.5 | p. 2, §1.2 | ✅ |
| Palabras clave | 1 | p. 2, §1.3 (las 8 de la guía) | ✅ |
| Equipo | 0.5 | p. 3, §3.1; Fig. 1 | ✅ |
| Procedimiento | 2.5 | p. 4–5, §3.2 (pasos 1–10); Figs. 1–4 | ✅ |
| Tablas o gráficos | 0.5 | Cuadros 1–8; Figs. 9–12 | ✅ |
| Tratamiento estadístico | 4 | p. 9 (§4.3), p. 11–13 (§5.1–5.4) | ✅ |
| Describe resultados | 0.5 | §4–5 | ✅ |
| Características cualitativas | 2 | p. 13, Cuadro 7; p. 10, Fig. 8 | ✅ |
| Cóncavo vs. convexo y trazado | 1 | p. 7 (§4.1, incluye d_o = f); p. 15 (§6.1) | ✅ |
| Interpreta el gráfico y justifica el ajuste | 3 | p. 11 (§5.1); p. 15 (§6.2) | ✅ |
| Fuentes de error y mejoras | 1 | p. 16, §6.4 y §6.6 | ✅ |
| Conclusión (discusión) | 1 | p. 17, §7 | ✅ |
| Reflexión adicional | 4 | §5.2, §5.4, §5.6, §6.2, §6.3, §6.7 | ✅ |
| Descuento por resultados no obtenidos (−2) | | Las hipótesis usan "podría", "posible" y "no verificado"; las características que salen de M dicen "según M" | ✅ sin riesgo |
| Descuento por alteración de datos (−5) | | Cuadros 1–2 = hoja firmada; d_o = R se conserva tal como está | ✅ sin riesgo |

---

## 3. Requisitos de la guía y de entrega

| Requisito | Evidencia | Estado |
|---|---|---|
| Diagramas A y B firmados | Figs. 5–6 | ✅ |
| Tabla C firmada y completa | Fig. 7 | ✅ |
| Interpretar d_o = f (rayos paralelos) | §4.1 | ✅ |
| Al menos 6 mediciones, separadas uniformemente | 7 (6 cada 5 cm + caso extremo) | ✅ |
| Fotos como evidencia, incluido el convexo (ítem 18) | Figs. 1–4 y 8 | ✅ |
| Gráficas y cálculos en el documento | §4–5 | ✅ |
| **Enlace al video de YouTube** | p. 2: [PENDIENTE] | ❌ |
| **Enlace a los datos experimentales** | p. 2: [PENDIENTE] | ❌ |
| Recuadro rojo de pendientes | p. 2 | ❌ borrar al entregar |

---

## 4. Hallazgos nuevos (todos de redacción, sin impacto en la nota)

| # | Dónde | Problema | Acción propuesta |
|---|---|---|---|
| R1 | p. 15, §6.2: "los siete puntos quedan **sobre ella**" | Ambiguo: "ella" puede leerse como la recta experimental. Se refiere a que los puntos quedan por encima de la recta **teórica**. | Cambiar a "quedan por encima de la teórica". |
| R2 | p. 13, Cuadro 7, fila del convexo: "No se **forma** en pantalla" | Las demás filas están en pasado ("se formó", "se proyectó"). | Cambiar a "No se formó en la pantalla". |

Revisé la maquetación de las páginas 9 y 13: fórmulas, Cuadros 1, 2, 5, 6 y 7. No hay desbordes ni texto cortado.

---

## 5. Coherencia con `guion_video.md`

| Punto | Estado |
|---|---|
| Valores numéricos citados en el guion | ✅ Coinciden con el informe |
| "Según la magnificación" en lugar de "vimos" (escenas 6 y 8) | ✅ |
| Hipótesis δ y causa del descarte en condicional | ✅ |
| Cinco fuentes de error (escena 9) | ✅ |
| Caso d_o = f (escena 2) | ✅ |
| Números de figuras y cuadros citados (Figs. 1–12, Cuadros 1–8) | ✅ Sin cambios de numeración tras la versión concisa |

---

## 6. Pendientes, por prioridad

1. **Obligatorio:** grabar y subir el video, y pegar los dos enlaces en p. 2.
2. **Obligatorio:** borrar el recuadro rojo de pendientes.
3. **Opcional:** corregir R1 y R2 (dos cambios de palabras).

**Conclusión:** el informe está completo, sin errores de cálculo ni riesgos de descuento. Solo faltan los enlaces de entrega.
