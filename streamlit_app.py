import streamlit as st

import datetime
import time
from PIL import Image


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(
    "# 🤯 1. Titulok, Nadpis (Title)"
)
st.title("😎 Moja aplikacia s Widgetmi a komponentami")

st.write(
    "# 🔠 2. Text (Text)"
)
st.write("Toto je klasicky text")
st.write(
    "# ▶️ 3. Tlačidlo (Button)"
)
if st.button("Knikni na mňa"):
    st.write("Si klikol na tlacidlo")
st.write(
    "# 🛝 4. Posuvník (slider)"
)
cislo = st.slider("Vyber cislo", 0, 100, 50)
st.write(f"Vybrali ste cislo {cislo}")
st.write(
    "# ✍️ 5. Textový vstup (Text Input)"
)
meno = st.text_input("Zadajte svoje meno: ")
st.write(f"Ahoj, {meno} 👍")
st.write(
    "# ☑️ 6. Zaškrtávacie políčko. (Checkbox)"
)
akcia = st.checkbox("Zobrazit text")
if akcia:
    st.write("Text je zobrazeny 😎")
st.write(
    "# 🔽 8. Rozbaľovací zoznam s možnosťami. (Selectbox)"
)
volba = st.selectbox("Vyberte moznost: ", ["Moznost 1", "Moznost 2", "Moznost 3"])
st.write(f"Vybrali ste, {volba} 👍")


st.write(
    "# 📁 9. Upload súborov. (File uploader)"
)
subor = st.file_uploader("Nahrajte subor")
if subor is not None:
    st.write("Subor uspesne nahrany")


st.write(
    "# 🔥 10. Upload CSV súborov. (File CSV uploader)"
)
upload_subor = st.file_uploader("Nahrajte CSV subor: ", type="csv")
if upload_subor is not None:
    df = pd.read_csv(upload_subor)
    st.write("Toto su nase data: ")
    st.dataframe(df)


upload_obrazok = st.file_uploader("Nahrajte obrazok: ", type = ["jpg", "jpeg", "png"])
if upload_obrazok is not None:
    obrazok = Image.open(upload_obrazok)
    st.image(obrazok, caption = "Nahrany obrazok", use_column_width=True)
    