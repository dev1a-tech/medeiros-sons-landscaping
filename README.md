# Medeiros & Sons Landscaping — Website

Concept one-page website for **Medeiros & Sons Landscaping** in North Dartmouth, MA (508-636-4662).
It's mobile-friendly, with click-to-call buttons, services, a service area, FAQs and a free-estimate form.

![Website preview](screenshots/desktop.png)

## Live site

- **GitHub Pages:** https://YOUR-USERNAME.github.io/medeiros-sons-landscaping/
- **Streamlit:** https://YOUR-APP-NAME.streamlit.app

## Files

| File | What it does |
|---|---|
| `index.html` | The website. Open it in any browser. |
| `build_site.py` | Python script that builds `index.html`. Edit the `CONFIG` section to change the text. |
| `app.py` | Streamlit version of the site. |
| `requirements.txt` | Packages Streamlit needs to install. |
| `screenshots/` | Preview images. |

## Run it on a Mac

```
python3 build_site.py              # rebuilds index.html and opens it
pip3 install -r requirements.txt
python3 -m streamlit run app.py    # runs the Streamlit version
```

## Built with

Python · HTML · CSS · Streamlit

---

*Concept site. Not the official website of Medeiros & Sons Landscaping.*
