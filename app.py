import streamlit as st
from database import initiera_databas, lägg_till_bolag, hämta_alla_bolag, uppdatera_bolag, ta_bort_bolag

st.set_page_config(page_title="Aktieanalysapp", layout="wide")
initiera_databas()

st.title("📈 Aktieanalys med P/S-tal")

with st.form("lägg_till_formulär"):
    st.subheader("➕ Lägg till nytt bolag")
    bolagsnamn = st.text_input("Bolagsnamn")
    nuvarande_kurs = st.number_input("Nuvarande kurs", value=0.0)
    omsättning_i_år = st.number_input("Omsättning i år", value=0.0)
    omsättning_nästa_år = st.number_input("Omsättning nästa år", value=0.0)
    antal_aktier = st.number_input("Antal utestående aktier", value=0)
    ps_tal = [st.number_input(f"P/S-tal {i+1}", value=0.0) for i in range(5)]
    skicka = st.form_submit_button("Lägg till bolag")
    if skicka and bolagsnamn:
        lägg_till_bolag(bolagsnamn, nuvarande_kurs, omsättning_i_år, omsättning_nästa_år, antal_aktier, *ps_tal)
        st.success("Bolaget har lagts till.")
        st.session_state["refresh"] = True

def beräkna_pot_kurs(omsättning, aktier, ps):
    return (omsättning / aktier) * ps if aktier > 0 else 0

bolag = hämta_alla_bolag()
if bolag:
    st.header("📋 Bolagslista")
    tabell_data = []
    for b in bolag:
        id, namn, kurs, oms_år, oms_nästa, aktier, ps1, ps2, ps3, ps4, ps5 = b
        ps_medel = (ps1 + ps2 + ps3 + ps4 + ps5) / 5
        kurs_idag = beräkna_pot_kurs(oms_år, aktier, ps_medel)
        kurs_slut = beräkna_pot_kurs(oms_nästa, aktier, ps_medel)
        undervärdering = ((kurs_slut - kurs) / kurs) * 100 if kurs > 0 else 0
        tabell_data.append({
            "ID": id,
            "Bolag": namn,
            "Nuvarande kurs": kurs,
            "Potentiell kurs idag": round(kurs_idag, 2),
            "Potentiell kurs slut året": round(kurs_slut, 2),
            "Undervärdering (%)": round(undervärdering, 2),
        })
    tabell_data.sort(key=lambda x: x["Undervärdering (%)"], reverse=True)
    st.dataframe(tabell_data, use_container_width=True)
