# 📊 Aktieanalysapp

En enkel Streamlit-app för att analysera aktier baserat på omsättning och P/S-tal.

## 🗂 Struktur

- `app.py` – Huvudfilen för Streamlit-appen
- `database.py` – SQLite-hantering
- `mnt/data/.keep` – Säkerställer att mappen inte raderas i Streamlit Cloud
- `.streamlit/config.toml` – Streamlit-konfiguration
- `requirements.txt` – Beroenden

## 🧑‍💻 Så kör du

1. Klona projektet
2. Kör `streamlit run app.py`
3. Använd Streamlit Cloud om du kör på iPhone

Data sparas i `mnt/data/database.db` och raderas inte vid omstart.