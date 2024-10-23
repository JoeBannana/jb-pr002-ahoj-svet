import streamlit as st
import pandas as pd
import datetime
import time
from PIL import Image

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
    "# ✍ 5. Textový vstup (Text Input)"
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

# st.write(
#     "# 🔥 10. Upload CSV súborov. (File CSV uploader)"
# )

# upload_subor = st.file_uploader("Nahrajte CSV subor: ", type="csv")

# if upload_subor is not None:
#     df = pd.read_csv(upload_subor)

#     st.write("Toto su nase data: ")
#     st.dataframe(df)


# st.write(
#     "# 🏁 11. Upload obrázkov. (File image uploader)"
# )

# upload_obrazok = st.file_uploader("Nahrajte obrazok: ", type = ["jpg", "jpeg", "png"])

# if upload_obrazok is not None:
#     obrazok = Image.open(upload_obrazok)
#     st.image(obrazok, caption = "Nahrany obrazok", use_column_width=True)


# st.write(
#     "# 📥 12. Tlačidlo na stiahnutie. (Download button)"
# )

# # Konvertovanie pandas dataframe do CSV
# csv = df.to_csv(index=False)

# st.download_button(
#     label = "Stiahnut CSV",
#     data = csv,
#     file_name="filmy.csv",
#     mime = "text/csv"
# )


st.write(
    "# 📻 13. Výber jednej možnosti. (Radio)"
)

volba = st.radio("Vyberte oblubeny zaner filmu: ", ("Akcne", "Komedie", "Drama"))

if volba == "Akcne":
    st.write("Vybrali si akcne filmy")
elif (volba == "Komedie"):
    st.write("Vybrali si komedie")
else:
    st.write("Vybrali si Drama")


vybrane_filmy = st.multiselect(
    "Vyberte svoje oblubene filmy",
    ["Matrix", "Pan prsten", "Star Wars", "Inception"],
    placeholder= "Vyberte film, ktory sa vam paci"
)

st.write(f"Vybrali ste: {', '.join(vybrane_filmy)}")

st.write(
    "# 📅 14. Výber dátumu. (Date input)"
)

datum = st.date_input(
    "Vyberte datum",
    datetime.date(2024,5,31)
)

st.write("Vybrali ste datum: ", datum)

st.write(
    "# 🕔 15. Výber času. (Time input)"
)

cas = st.time_input(
    "Zadajte cas",
    datetime.time(15, 30, 50)
)

st.write("Vybrali ste cas: ", cas)

st.write(
    "# 🅰 16. Vstup dlhšieho textu. (Text area)"
)

text = st.text_area(
    "Napiste svoj nazor na film",
    "Zadajte text sem"
)

st.write("Vas nazor: ", text)

st.write(
    "# 🔢 17. Vstup číselnej hodnoty. (Number Input)"
)

hodnotenie = st.number_input(
    "Zadajte hodnotenie filmu (od 1 do 10)",
    min_value=1,
    max_value=10,
    value=5,
)

st.write(f"Vase hodnotenie {hodnotenie}/10")

st.write(
    "# 🎚️ 18. Posuvník s výberom. (Select Slider)"
)

stupnica = st.select_slider(
    "Ako velmi sa vam pacil film?",
    options=["Hrozne", "Slabe", "Priemerne", "Dobre", "Vyborne"],
    value="Dobre"
)

st.write(f"Vase hodnotenie: {stupnica}")

st.write(
    "# 🔴 19. Výber farby (Color picker)"
)

farba = st.color_picker(
    "Vyberte farbu pozadia",
    "#00F900"
)

st.write(f"Vasa farba: {farba}")


st.write(
    "# ⏳ 20. Indikátor progresu (Progress)"
)

# progres = st.progress(0)

# for i in range(1000):
#     time.sleep(0.05)
#     progres.progress(i + 1)

st.write(
    "# 📐 21. Zobrazenie LaTeXu (matematické výrazy) (latex)"
)

st.latex(r'''
     a^2 + b^2 = c^2
     ''')


st.write(
    "# 🌍 22. Zobrazenie kódu s formátovaním (code)"
)

st.code('''
def ahoj():
    print("Ahoj, Streamlit!")
''', language='python')



st.write(
    "# 🌐 23. Zobrazenie JSON dát (json)"
)

data = {
    'meno': 'Peter',
    'vek': 30,
    'zamestnanie': 'programátor'
}
st.json(data)

st.write(
    "# ➡️ 24. Dynamický widget (všestranný) (write)"
)

st.write("Textový reťazec")
st.write(123)
st.write({'kľúč': 'hodnota'})

st.write(
    "# 📏 25. Zobrazenie kľúčových metrik (metric)"
)

st.metric(label="Teplota", value="24°C", delta="2°C")

# Zobrazenie chybovej správy
st.error("Toto je chybové hlásenie!")

st.write(
    "# ✅ 27. Zobrazenie úspešnej správy (success)"
)

# Zobrazenie úspešnej správy
st.success("Úloha bola úspešne dokončená!")

st.write(
    "# ⚠️ 28. Zobrazenie varovnej správy (warning)"
)

# Zobrazenie varovania
st.warning("Toto je varovanie!")

st.write(
    "# 🆗 29. Zobrazenie informatívnej správy (info)"
)

# Zobrazenie informatívnej správy
st.info("Toto je informatívna správa.")




st.write(
    "# ❗ 30. Zobrazenie výnimky (chyby v kóde) (exception)"
)

#Zobrazenie výnimky
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     st.exception(e)

st.write(
    "# 🌀 31. Zobrazenie spinneru počas načítavania (spinner)"
)

# Spinner počas načítavania
with st.spinner('Čakajte prosím...'):
    time.sleep(5)
st.success('Hotovo!')

st.write(
    "# 📝 32. Zobrazenie textovej poznámky (caption)"
)

st.caption('Toto je poznámka alebo vysvetlenie.')



st.write(
    "# 🖼️ 33. Zobrazenie obrázkov (image)"
)

# Zobrazenie obrázku
st.image("https://eurocc.nscc.sk/wp-content/uploads/2020/12/CC_EURO-_logo_gold-1.png", caption='Logo NSC')

st.write(
    "# 🎞️ 34. Zobrazenie videa/audio (video/audio)"
)

# Zobrazenie videa
st.video("https://www.youtube.com/watch?v=xG5X5n9cmHg")


st.write(
    "# 🏛️ 35. Rozdelenie obrazovky do stĺpcov (columns)"
)

# Vytvorenie 3 stĺpcov
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Stĺpec 1")

with col2:
    st.write("Stĺpec 2")

with col3:
    st.write("Stĺpec 3")

st.write(
    "# 📑 36. Vytváranie záložiek/tabov (tabs)"
)

# Vytvorenie záložiek
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Obsah pre záložku 1")

with tab2:
    st.write("Obsah pre záložku 2")

with tab3:
    st.write("Obsah pre záložku 3")

st.write(
    "# 🚀 37. Rozbalovací blok (expander)"
)

with st.expander("Kliknite sem pre viac informácií"):
    st.write("Toto je rozbalený obsah.")

st.write(
    "# 📈 38. Zobrazenie grafov v Matplotlib (pyplot)"
)

import matplotlib.pyplot as plt
# Vytvorenie jednoduchého grafu
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

# Zobrazenie grafu
st.pyplot(fig)