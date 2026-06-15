import plotly.graph_objects as go
import streamlit as st
import math

v_cross = None
p1_array = [0, 0, 0]
st.title("Vektor-Visualisierung")
ax, ay, az = 0.0, 0.0, 0.0
bx, by, bz = 0.0, 0.0, 0.0
cx, cy, cz = 0.0, 0.0, 0.0
eingabe_modus = st.radio( label="Was möchtest du eingeben?", options=["Vektoren (v und w)", "3 Punkte (A, B, C)"] )
if eingabe_modus == "3 Punkte (A, B, C)":
    st.write("### Punkte eingeben")
    c1, c2, c3 = st.columns(3)
    with c1:
        ax = st.number_input("A: x", value=0.0)
        ay = st.number_input("A: y", value=0.0)
        az = st.number_input("A: z", value=0.0)
    with c2:
        bx = st.number_input("B: x", value=1.0)
        by = st.number_input("B: y", value=0.0)
        bz = st.number_input("B: z", value=0.0)
    with c3:
        cx = st.number_input("C: x", value=0.0)
        cy = st.number_input("C: y", value=1.0)
        cz = st.number_input("C: z", value=0.0)
        vx = bx - ax
        vy = by - ay
        vz = bz - az
        wx = cx - ax
        wy = cy - ay
        wz = cz - az
else:
    st.write("### Vektoren direkt eingeben")
    col_v = st.columns(3)
    with col_v[0]:
        vx = st.number_input("v: x", value=1.0, key="vx_v")
    with col_v[1]:
        vy = st.number_input("v: y", value=1.0, key="vy_v")
    with col_v[2]: vz = st.number_input("v: z", value=1.0, key="vz_v")
    col_w = st.columns(3)
    with col_w[0]:
        wx = st.number_input("w: x", value=0.0, key="wx_v")
    with col_w[1]:
        wy = st.number_input("w: y", value=1.0, key="wy_v")
    with col_w[2]:
        wz = st.number_input("w: z", value=0.0, key="wz_v")
with st.expander("Rotes Dreick"):
      p1x = st.slider("start P1 X", -10, 10, 0)
      p1y = st.slider("start P1 Y", -10, 10, 0)
      p1z = st.slider("start P1 Z", -10, 10, 0)
      bx= st.slider("Punkt B X", -10.0, 10.0, 5.0)
      by= st.slider("Punkt B Y", -10.0, 10.0, 0.0)
      bz= st.slider("Punkt B Z", -10.0, 10.0, 0.0)
      cx= st.slider("Punkt C X", -10.0, 10.0, 0.0)
      cy= st.slider("Punkt C Y", -10.0, 10.0, 5.0)
      cz= st.slider("Punkt C Z", -10.0, 10.0, 0.0)
laenge_v = math.sqrt(vx**2 + vy**2 + vz**2)
laenge_w = math.sqrt(wx**2 + wy**2 + wz**2)
skalarprodukt_wert = vx*wx + vy*wy + vz*wz
vwx = vy*wz - vz*wy
vwy = vz*wx - vx*wz
vwz = vx*wy - vy*wx
flaech = math.sqrt(vwx**2 + vwy**2 + vwz**2)
import math
if laenge_v > 0 and laenge_w > 0:
    cos_phi = skalarprodukt_wert / (laenge_v * laenge_w)
    cos_phi = max(-1.0, min(1.0, cos_phi))
    winkel_grad = math.degrees(math.acos(cos_phi))
else:
    winkel_grad = 0
    st.subheader("Länge der Vektoren")
    col_l1, col_l2 = st.columns(2)
    col_l1.metric("Länge von v", f"{laenge_v:.2f}")
    col_l2.metric("Länge von w", f"{laenge_w:.2f}")
st.divider()
st.write(f"Der Vektor v w x ist: **[{round(vwx, 2)}, {round(vwy, 2)}, {round(vwz, 2)}]**")
fig = go.Figure()
fig.add_trace(go.Scatter3d(x=[ax, ax+vx], y=[ay, ay+vy], z=[az, az+vz], mode="lines", line=dict(color="blue", width=6),name="Vektor v"))
fig.add_trace(go.Cone(x=[ax+vx], y=[ay+vy], z=[az,vz], u=[vx], v=[vy], w=[wz], sizemode="absolute", showscale=False, name="Spitze v"))
fig.add_trace(go.Scatter3d(x=[ax, ax+wx], y=[ay, ay+wy], z=[az, az+wz], mode="lines", line=dict(color="green", width=6), name="Vektor w"))
fig.add_trace(go.Cone(x=[ax+wx], y=[ay+wy], z=[az+wz], u=[wx], v=[wy], w=[wz], sizemode="absolute", showscale=False, name="Spitze w"))
fig.add_trace(go.Scatter3d(x=[ax, ax+vwx], y=[ay, ay+vwy], z=[az, az+vwz], mode="lines", line=dict(color="red", width=6), name="Kreuzprodukt"))
fig.update_layout(scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))
st.plotly_chart(fig)
st.divider()
st.subheader("Mathematischer Hintergrund")
st.write("Das **Kreuzprodukt** (Normalenvektor) wird wie folgt berechnet:")
st.latex(r"\vec{v} \times \vec{w} = \begin{pmatrix} v_y w_z - v_z w_y \\ v_z w_x - v_x w_z \\ v_x w_y - v_y w_x \end{pmatrix}")
st.info("Der resultierende Vektor steht immer senkrecht auf der Ebene, die von v und w aufgespannt wird.")
with st.expander("Rechenweg für dein Kreuzprodukt anzeigen"):

    st.write("Setzen wir deine Werte in die Formel ein:")

    st.latex(
        rf"""
\vec{{vw}} =
\begin{{pmatrix}}
{vy} \cdot {wz} - {vz} \cdot {wy} \\
{vz} \cdot {wx} - {vx} \cdot {wz} \\
{vx} \cdot {wy} - {vy} \cdot {wx}
\end{{pmatrix}}
"""
    )

    st.write("---")
    st.write(f"**Dein Ergebnis:**")

    st.latex(rf"\vec{{vw}} = \begin{{pmatrix}} {vwx:.1f} \\ {vwy:.1f} \\ {vwz:.1f} \end{{pmatrix}}")
flaeche = (vwx**2 + vwy**2 + vwz**2)**0.5
st.divider()
st.write("Die Fläche $A$ des Parallelogramms berechnet man über den Betrag des Kreuzprodukts:")
st.latex(r"A = |\vec{v} \times \vec{w}| = |\vec{vw}| = \sqrt{vwx^2 + vwy^2 + vwz^2}")
with st.expander("Rechenweg für den Flächeninhalt anzeigen"):
    st.write("Wir setzen deinen berechneten Wert ein:")
    st.latex(rf"A = \\sqrt{{{vwx:.1f}^2 + {vwy:.1f}^2 + {vwz:.1f}^2}}")
    st.write(f"Das ergibt eine Fläche von: **{flaeche:.2f} FE**")
st.divider()
st.subheader("Fläche des Dreiecks")
st.latex(r"A_{Dreieck} = \frac{1}{2} \cdot A_{Parallelogramm}")
with st.expander("Rechenweg für die Dreiecksfläche anzeigen"):
    st.write("Das von den Vektoren aufgespannte Dreieck ist genau halb so groß wie das Parallelogramm:")
    dreieck = flaeche / 2
    st.latex(r"A_{Dreieck} = \frac{1}{2} \cdot" + f"{flaeche:.2f} = {dreieck:.2f}")
    st.success(f"Die Dreiecksfläche beträgt: {dreieck:.2f} FE")
st.header("Ergebnisse der Analyse")
c1, c2 = st.columns(2)
c1.metric("Länge Vektor v", f"{laenge_v:.2f}")
c2.metric("Länge Vektor w", f"{laenge_w:.2f}")
c3, c4 = st.columns(2)
skalar_de = f"{skalarprodukt_wert:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
st.metric(label="skalarprofukt", value=skalar_de)
winkel_de = f"{winkel_grad:.1f}".replace(".", ",") + "°"
st.metric(label="winkel zwischen v und w", value=winkel_de)
if skalarprodukt_wert == 0:
    st.success("Die Vektoren stehen senkrecht (orthogonal) aufeinander! ⊥")