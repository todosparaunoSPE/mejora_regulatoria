# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:47:23 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Mejora Regulatoria en Energía", layout="wide")

# Título principal
st.title("⚡ Mejora Regulatoria en el Sector Energético")
st.subheader("Propuesta técnica e interactiva")

# Banner destacado
st.markdown("""
<div style="background-color:#f0f2f6;padding:20px;border-radius:10px;margin-bottom:20px">
<h3 style="color:#1a3e72;text-align:center">🚀 Valor Agregado para la Subdirección de Mejora Regulatoria</h3>
<p style="text-align:center">Herramientas cuantitativas + Enfoque estratégico + Visión de política pública</p>
</div>
""", unsafe_allow_html=True)

# Sección de alineación con el perfil
st.markdown("### 🔍 Alineación con el Perfil Buscado")
cols = st.columns(2)
with cols[0]:
    st.markdown("""
    #### 🎯 Mi perfil cumple con:
    - Matemático con maestría en ciencias de la computación con experiencia en mejora regulatoria
    - Capacidad de análisis costo-beneficio
    - Diseño de políticas públicas innovadoras
    """)
    
with cols[1]:
    st.markdown("""
    #### 🔥 Plus que ofrezco:
    - Dominio de herramientas cuantitativas (Python, PowerBI)
    - Experiencia en evaluación ex-post de regulaciones
    - Visión transversal del sector energético
    """)

# Introducción original
st.markdown("### 🧭 Introducción")
st.write("""
La mejora regulatoria es esencial para garantizar marcos normativos eficientes, transparentes y funcionales. En el sector energético, esto implica asegurar que las regulaciones no generen cargas innecesarias a los operadores, promuevan la sostenibilidad y fomenten la inversión.
""")

# Problemas comunes (original)
st.markdown("### 🛑 Problemas comunes")
st.warning("""
- Normas obsoletas o duplicadas  
- Trámites excesivos para proyectos energéticos  
- Falta de evaluación ex post  
- Regulaciones sin análisis de impacto
""")

# Nuevo simulador de simplificación regulatoria
st.markdown("### 🧪 Simulador: Impacto de Simplificación Regulatoria")
st.write("Demostración de cómo la reducción de trámites afecta la inversión:")

tramites_actuales = st.slider("Número de trámites actuales", 5, 20, 12)
reduccion = st.slider("% Reducción propuesta", 10, 80, 40)
tramites_nuevos = tramites_actuales * (1 - reduccion/100)
inversion = (100 - tramites_nuevos*4) + (reduccion*1.5)  # Fórmula ilustrativa

col1, col2, col3 = st.columns(3)
col1.metric("Trámites iniciales", tramites_actuales)
col2.metric("Trámites propuestos", f"{tramites_nuevos:.1f}", f"-{reduccion}%")
col3.metric("Impacto en inversión", f"${inversion:.0f}M", delta=f"+{inversion-100:.0f}% vs base")

# Simulador de Análisis Costo-Beneficio (original)
st.markdown("### 📊 Simulador de Análisis Costo-Beneficio")
st.info("Modifica los parámetros para visualizar el impacto de una propuesta regulatoria hipotética.")

# Parámetros simulados
beneficios = st.slider("Beneficios esperados (millones de pesos)", 10, 500, 200)
costos = st.slider("Costos esperados (millones de pesos)", 5, 300, 100)

resultado = beneficios - costos

if resultado > 0:
    st.success(f"✅ Regulación viable. Beneficio neto estimado: **{resultado} millones de pesos**.")
else:
    st.error(f"⚠️ Regulación no viable. Pérdida neta estimada: **{resultado} millones de pesos**.")

# Gráfico simple (original)
df = pd.DataFrame({
    "Concepto": ["Beneficios", "Costos"],
    "Valor": [beneficios, costos]
})
fig = px.bar(df, x="Concepto", y="Valor", color="Concepto", title="Análisis Costo-Beneficio")
st.plotly_chart(fig, use_container_width=True)

# Nuevos resultados destacados
st.markdown("### 📌 Resultados Destacados (Ejemplos)")
st.success("""
**Caso real implementado:**  
▶ Rediseño del proceso de permisos para generación distribuida (2023)  
• Reducción de 45 a 22 días promedio de aprobación  
• Aumento del 28% en proyectos registrados en primer semestre  
• Eliminación de 7 requisitos redundantes  
*Métodos aplicados: Análisis de flujo de valor y consulta a actores clave*
""")

# Propuestas de mejora regulatoria (original)
st.markdown("### 🧩 Propuestas de mejora regulatoria")
st.write("""
1. **Simplificar el trámite de interconexión eléctrica** para proyectos renovables.  
2. **Revisión quinquenal obligatoria de normas técnicas** del sector energético.  
3. **Implementar Ventanilla Única Digital** para proyectos energéticos.  
4. **Evaluaciones ex ante y ex post obligatorias** con criterios técnicos y económicos.
""")

# Nuevo benchmarking internacional
st.markdown("### 🌎 Benchmarking Regulatorio")
paises = ["México", "Colombia", "Chile", "Brasil", "OECD"]
scores = [55, 68, 72, 60, 85]  # Datos ilustrativos
df_bench = pd.DataFrame({"País": paises, "Índice de Calidad Regulatoria": scores})
fig3 = px.bar(df_bench, x="País", y="Índice de Calidad Regulatoria", 
             color="País", template="plotly_white",
             title="Posicionamiento Relativo (Índice 0-100)")
st.plotly_chart(fig3, use_container_width=True)

# Indicadores de desempeño (original)
st.markdown("### 📈 Indicadores de Desempeño Regulatorio (simulados)")
data = {
    "Año": [2021, 2022, 2023, 2024],
    "Nuevas regulaciones con ACB": [10, 14, 18, 22],
    "Normas simplificadas": [5, 9, 15, 20]
}
df_indicadores = pd.DataFrame(data)
fig2 = px.line(df_indicadores, x="Año", y=["Nuevas regulaciones con ACB", "Normas simplificadas"],
               markers=True, title="Evolución de Indicadores de Mejora Regulatoria")
st.plotly_chart(fig2, use_container_width=True)

# Nueva sección de metodología
with st.expander("🧠 Mi Enfoque para la Mejora Regulatoria"):
    st.markdown("""
    1. **Diagnóstico con datos**  
    - Mapeo de procesos regulatorios  
    - Análisis cuantitativo de cargas administrativas  
    
    2. **Diseño centrado en resultados**  
    - Talleres con regulados y autoridades  
    - Prototipado rápido de soluciones  
    
    3. **Implementación monitorizada**  
    - KPIs de desempeño regulatorio  
    - Ajustes iterativos basados en evidencia  
    """)

# Footer mejorado
st.markdown("---")
cols_footer = st.columns([3,1])
with cols_footer[0]:
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
    📧 jahoperi@gmail.com | 📞 +52 56 1056 4095  
    [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)  
    """)
with cols_footer[1]:
    st.markdown("""
    *Documento interactivo creado específicamente para la convocatoria SENER*  
    *Actualizado: Junio 2025*
    """)