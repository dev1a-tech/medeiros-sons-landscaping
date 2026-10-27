# Medeiros & Sons Landscaping — Website

Concept one-page website for **Medeiros & Sons Landscaping**, North Dartmouth, MA (508-636-4662).
It's mobile-friendly, with click-to-call buttons, a services section, a service area, FAQs and a free-estimate form.

![Desktop preview](screenshots/desktop.png)

---

## What's in this folder

| File | What it is |
|---|---|
| `index.html` | **The website.** Double-click it to view it in your browser. |
| `build_site.py` | Python script that creates `index.html` from the settings at the top of the file. |
| `screenshots/` | Preview images of the site on desktop and on a phone. |
| `README.md` | This file. |

> **You don't need Python just to see the website.** `index.html` is already built. Double-click it.

---

## 1. View the website on your computer

1. Download or unzip this folder.
2. Double-click **`index.html`**.
3. It opens in Chrome, Edge, Safari or Firefox.

---

## 2. Change the text and rebuild (optional)

Use this only if you want to change the business details.

1. Install Python 3 from <https://www.python.org/downloads/>.
   On Windows, check **"Add Python to PATH"** during setup.
2. Open `build_site.py` in any text editor (Notepad works) and edit the `CONFIG` section near the top.
   Phone, services, towns, FAQs and hours are all set there.
3. Run the script:
   - **Windows:** open the folder, click the address bar, type `cmd`, press Enter, then run:
     ```
     py build_site.py
     ```
   - **Mac:** open Terminal, type `cd ` (with a space), drag the folder into the window, press Enter, then run:
     ```
     python3 build_site.py
     ```
4. A fresh `index.html` is created and opens in your browser.

**The black window is normal.** It's the Python terminal. The website itself opens in your browser, not in that window.

---

## 3. Put it online free with GitHub Pages

1. Create a new **public** repository named `medeiros-sons-landscaping`.
2. Click **Add file → Upload files** and drag in **everything in this folder**.
   `index.html` must be at the top level, not inside another folder.
3. Click **Commit changes**.
4. Go to **Settings → Pages**.
5. Under **Branch**, choose **`main`** and **`/ (root)`**, then click **Save**.
6. Wait 1–2 minutes, then refresh. Your link appears at the top:
   `https://YOUR-USERNAME.github.io/medeiros-sons-landscaping/`

### Troubleshooting

| Problem | Fix |
|---|---|
| A black window flashes and closes | That's normal for Python. Open `index.html` to see the site. |
| `python` is not recognized | Reinstall Python and check **"Add Python to PATH"**, or use `py` instead of `python`. |
| GitHub shows code instead of the website | You're viewing the file on GitHub. Use the **Pages link** from Settings → Pages instead. |
| GitHub Pages shows a 404 error | Make sure `index.html` is at the top level of the repo, the repo is public, and you waited a couple of minutes. |
| Changes don't appear online | Re-upload the new `index.html`, then wait a minute and hard-refresh (Ctrl+F5 / Cmd+Shift+R). |

---

## Before going live, confirm with the owner

Items marked `# CONFIRM` in `build_site.py` are placeholders:

- Services offered, towns served, "Free estimates", and the FAQ answers
- Business hours (currently "Call for availability")
- A real Google review link and a real customer review (used with permission)
- Real project photos for the gallery
- A form service (such as Formspree) for the quote form. Until one is added, the form asks visitors to call.

---

*Concept site. Not yet the official website of Medeiros & Sons Landscaping.*
