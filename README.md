# ✦ Celestia — AI Astrology Web App

A premium, fully offline astrology web service. Enter your birth details and receive a personalized natal chart reading covering your Sun, Moon, Rising signs, all planetary positions, and rich interpretations — no API keys required.

---

## Features

- **Premium dark cosmic UI** — glassmorphism, animated starfield, zodiac glyphs
- **Accurate birth charts** — powered by Swiss Ephemeris via Kerykeion
- **Full interpretations** — personality, challenges, love, career, life path
- **Inner planets** — Mercury, Venus, Mars, Jupiter, Saturn readings
- **Element & modality balance** — visual bars
- **Export as PDF** — styled, print-ready
- **Export as Text** — clean plain-text file
- **Copy to clipboard** — one click

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11, Flask 3.0 |
| Astrology Engine | Kerykeion 4.x (Swiss Ephemeris) |
| Geocoding | Geopy + Nominatim (OpenStreetMap, free) |
| PDF Generation | ReportLab |
| Frontend | Vanilla JS, CSS3 (no framework) |
| Fonts | Cinzel + Raleway (Google Fonts) |
| Deployment | Render (free tier) |

---

## Local Development

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/celestia-astrology.git
cd celestia-astrology

# Create virtualenv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install
pip install -r requirements.txt

# Run
python app.py
# Open http://localhost:5000
```

---

## Deploy to Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` — click **Create Web Service**
5. Wait ~3 min for the first build. Done!

> Free tier on Render sleeps after inactivity — first load may take ~30s.

---

## How It Works

1. User fills in: **name, date of birth, birth time, birth place**
2. Flask geocodes the birth place via **OpenStreetMap Nominatim** (free, no key)
3. **Kerykeion** (Swiss Ephemeris) calculates all planetary positions for the exact birth moment
4. Rich interpretations are generated **entirely in Python** — no external AI API
5. Results are displayed in a premium reading page with export options

---

## Project Structure

```
celestia/
├── app.py                     # Flask routes
├── astrology/
│   ├── calculator.py          # Swiss Ephemeris chart calculations
│   └── interpretations.py     # All reading text + generators
├── templates/
│   ├── index.html             # Landing / form page
│   └── reading.html           # Results page
├── static/
│   ├── css/style.css          # Full premium stylesheet
│   └── js/
│       ├── main.js            # Starfield + form UX
│       └── reading.js         # Reveal animations + export
├── requirements.txt
├── Procfile                   # Render / gunicorn start command
└── render.yaml                # Render deployment config
```

---

*No data is stored. No API keys. Privacy-first.*
