#!/usr/bin/env python3
"""
build_site.py — generates a one-page website for Medeiros & Sons Landscaping.

Usage:
    Windows:   py build_site.py
    Mac/Linux: python3 build_site.py

    This writes index.html next to this script and opens it in your browser.

Everything a business owner would want to change lives in the CONFIG block
below. Items marked  # CONFIRM  are reasonable placeholders that should be
checked with the owner before the site goes live (nothing here is taken from
the business itself except the name, town and phone number).
"""

from pathlib import Path
from string import Template
from html import escape

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG — edit this, re-run the script
# ─────────────────────────────────────────────────────────────────────────────
CONFIG = {
    "name": "Medeiros & Sons",
    "tagline": "Landscaping",
    "town": "North Dartmouth, MA",
    "phone": "508-636-4662",
    "email": "",                       # CONFIRM — leave blank to hide
    "hours": "Call for availability",  # CONFIRM — no hours are posted yet
    "google_review_url": "#",          # CONFIRM — paste the Google review link
    "form_endpoint": "",               # e.g. a Formspree URL; blank = demo mode
    "promises": [                      # CONFIRM each one with the owner
        "Locally based in North Dartmouth",
        "Free estimates",
        "Residential & small commercial",
    ],
    "services": [                      # CONFIRM which services are offered
        ("mow", "Lawn Care & Mowing",
         "Weekly or bi-weekly cuts, trimming and edging so the lawn looks sharp all season."),
        ("leaf", "Spring & Fall Cleanups",
         "Leaves, debris and winter damage cleared out, beds reset and ready for the season."),
        ("bed", "Mulch & Garden Beds",
         "Fresh mulch, crisp bed edges and weeding that keeps planting areas tidy."),
        ("plant", "Planting & Shrubs",
         "New shrubs, perennials and trees chosen to thrive in South Coast soil and salt air."),
        ("stone", "Patios & Walkways",
         "Stone and paver hardscapes that add usable space and curb appeal."),
        ("snow", "Snow Removal",
         "Driveways and walkways cleared after New England storms."),
    ],
    "steps": [
        ("Call or request a quote", "Tell us about your property and what you have in mind."),
        ("Walkthrough & estimate", "We come out, look at the yard and give you a clear price."),
        ("We do the work", "On schedule, cleaned up after, with no surprises on the bill."),
        ("Ongoing care", "Keep it looking great with seasonal or recurring service."),
    ],
    "service_area": [                  # CONFIRM
        "North Dartmouth", "Dartmouth", "Westport", "New Bedford",
        "Fall River", "Fairhaven", "Acushnet", "Freetown",
    ],
    "faq": [                           # CONFIRM answers
        ("Do you give free estimates?",
         "Yes. Call or send the form and we'll set up a time to look at your property."),
        ("Do I need to sign a season-long contract?",
         "No. We offer one-time jobs as well as recurring weekly or seasonal service."),
        ("What areas do you serve?",
         "North Dartmouth and the surrounding South Coast towns. If you're nearby, just ask."),
        ("How soon can you start?",
         "It depends on the season. Spring fills up fast, so it's worth calling early."),
    ],
    "gallery": [                       # replace with real project photos
        "Front lawn — after weekly service",
        "Fresh mulch & edged beds",
        "Paver walkway install",
        "Fall cleanup — before / after",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# Small inline SVG icons (no external files needed)
# ─────────────────────────────────────────────────────────────────────────────
ICONS = {
    "mow":   '<path d="M3 17h13l3-6H7"/><circle cx="7" cy="19" r="2"/><circle cx="16" cy="19" r="2"/><path d="M19 11l2-6"/>',
    "leaf":  '<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19l8-8"/>',
    "bed":   '<path d="M3 18h18"/><path d="M6 18c0-3 2-5 3-5s3 2 3 5"/><path d="M12 18c0-4 2-7 4-7s3 3 3 7"/>',
    "plant": '<path d="M12 21v-9"/><path d="M12 12c0-4 3-7 7-7 0 4-3 7-7 7z"/><path d="M12 15c0-3-2-5-6-5 0 3 2 5 6 5z"/>',
    "stone": '<rect x="3" y="4" width="8" height="7" rx="1"/><rect x="13" y="4" width="8" height="7" rx="1"/><rect x="8" y="13" width="8" height="7" rx="1"/>',
    "snow":  '<path d="M12 2v20M4 7l16 10M20 7L4 17"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "phone": '<path d="M5 4h4l2 5-3 2a11 11 0 006 6l2-3 5 2v4a2 2 0 01-2 2A17 17 0 013 6a2 2 0 012-2"/>',
    "pin":   '<path d="M12 21s7-6 7-12a7 7 0 10-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "star":  '<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',
}

def icon(name, size=24):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

# ─────────────────────────────────────────────────────────────────────────────
# Section builders
# ─────────────────────────────────────────────────────────────────────────────
def build_promises(c):
    return "".join(f'<li>{icon("check", 18)}{escape(p)}</li>' for p in c["promises"])

def build_services(c):
    return "".join(
        f'<article class="card"><div class="card-icon">{icon(key, 28)}</div>'
        f'<h3>{escape(title)}</h3><p>{escape(desc)}</p></article>'
        for key, title, desc in c["services"])

def build_steps(c):
    return "".join(
        f'<li><span class="step-num">{i:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></li>'
        for i, (t, d) in enumerate(c["steps"], 1))

def build_gallery(c):
    tones = ["g1", "g2", "g3", "g4"]
    return "".join(
        f'<figure class="shot {tones[i % 4]}"><figcaption>{escape(cap)}</figcaption></figure>'
        for i, cap in enumerate(c["gallery"]))

def build_towns(c):
    return "".join(f"<li>{escape(t)}</li>" for t in c["service_area"])

def build_faq(c):
    return "".join(
        f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>"
        for q, a in c["faq"])

def build_service_options(c):
    return "".join(f"<option>{escape(t)}</option>" for _, t, _ in c["services"])

# ─────────────────────────────────────────────────────────────────────────────
# Page template ($placeholders are filled by string.Template)
# ─────────────────────────────────────────────────────────────────────────────
PAGE = Template(r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$name $tagline | $town</title>
<meta name="description" content="$name $tagline — lawn care, cleanups, planting and hardscapes in $town and the South Coast. Call $phone.">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LandscapingBusiness","name":"$name $tagline",
 "telephone":"$phone","address":{"@type":"PostalAddress","addressLocality":"North Dartmouth","addressRegion":"MA"}}
</script>
<style>
:root{
  --forest:#1f3d2b; --moss:#2f5d3a; --sage:#8fae7e; --leaf:#5c8a4a;
  --cream:#f6f2e9; --sand:#e9e1cf; --ink:#1b1f1c; --muted:#5b645d; --white:#fff;
  --radius:14px; --shadow:0 10px 30px rgba(31,61,43,.12);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--cream);line-height:1.6}
h1,h2,h3{font-family:Georgia,'Times New Roman',serif;line-height:1.15;color:var(--forest)}
a{color:inherit}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 24px;border-radius:999px;
     font-weight:600;text-decoration:none;border:2px solid transparent;cursor:pointer;font-size:1rem}
.btn-primary{background:#e3a63b;color:#1b1f1c}
.btn-primary:hover{background:#d39528}
.btn-ghost{border-color:var(--forest);color:var(--forest)}
.btn-ghost:hover{background:rgba(31,61,43,.08)}
.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;font-weight:600;color:var(--leaf)}
section{padding:88px 0}
.section-head{max-width:640px;margin-bottom:44px}
.section-head h2{font-size:clamp(1.9rem,3.6vw,2.7rem);margin:8px 0 12px}
.section-head p{color:var(--muted)}

/* top bar + nav */
.topbar{background:var(--forest);color:#dfe8da;font-size:.85rem}
.topbar .wrap{display:flex;justify-content:space-between;gap:12px;padding-top:8px;padding-bottom:8px}
.topbar span{display:inline-flex;align-items:center;gap:6px}
nav{background:var(--cream);position:sticky;top:0;z-index:20;border-bottom:1px solid var(--sand)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;height:72px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none}
.logo-mark{width:42px;height:42px;border-radius:50%;background:var(--moss);display:grid;place-items:center;color:#fff}
.logo b{font-family:Georgia,'Times New Roman',serif;font-size:1.25rem;color:var(--forest);display:block;line-height:1}
.logo small{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--leaf)}
.links{display:flex;gap:28px;align-items:center}
.links a{text-decoration:none;font-weight:500;color:var(--forest)}
.links .btn{padding:10px 18px}

/* hero */
.hero{position:relative;background:#eaf2e3;color:var(--ink);overflow:hidden;padding:0}
.hero-art{position:absolute;inset:0;width:100%;height:100%}
.hero .wrap{position:relative;padding-top:110px;padding-bottom:150px}
.hero h1{color:var(--forest);font-size:clamp(2.6rem,6vw,4.6rem);max-width:760px}
.hero h1 em{font-style:normal;color:#c27c12}
.hero p.lead{font-size:1.2rem;max-width:560px;margin:20px 0 32px;color:#3d4a40}
.hero-ctas{display:flex;gap:14px;flex-wrap:wrap}
.promises{list-style:none;display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:40px}
.promises li{display:flex;align-items:center;gap:8px;font-weight:600;color:var(--forest);background:rgba(255,255,255,.8);padding:6px 14px;border-radius:999px}
.promises svg{color:var(--leaf)}

/* services */
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:var(--white);border-radius:var(--radius);padding:30px;box-shadow:var(--shadow);
      transition:transform .2s}
.card:hover{transform:translateY(-4px)}
.card-icon{width:56px;height:56px;border-radius:12px;background:#e6efe0;color:var(--moss);
           display:grid;place-items:center;margin-bottom:18px}
.card h3{font-size:1.3rem;margin-bottom:8px}
.card p{color:var(--muted)}

/* process */
.process{background:var(--white)}
.steps{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:28px;counter-reset:s}
.steps li{border-top:3px solid var(--sage);padding-top:20px}
.step-num{font-family:Fraunces,serif;font-size:2.2rem;color:var(--sage)}
.steps h3{font-size:1.2rem;margin:6px 0}
.steps p{color:var(--muted)}

/* gallery */
.gallery{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:220px 220px;gap:16px}
.shot{border-radius:var(--radius);position:relative;overflow:hidden;display:flex;align-items:flex-end}
.shot:first-child{grid-row:span 2}
.shot:last-child{grid-column:span 2}
.shot figcaption{background:rgba(20,35,25,.72);color:#fff;font-size:.88rem;padding:8px 14px;margin:14px;border-radius:999px}
.g1{background:linear-gradient(160deg,#9cc17f 0%,#5c8a4a 55%,#2f5d3a 100%)}
.g2{background:linear-gradient(200deg,#c9a77c 0%,#8a6a45 60%,#5b452c 100%)}
.g3{background:linear-gradient(170deg,#d6d0c4 0%,#a59d8d 60%,#6f685b 100%)}
.g4{background:linear-gradient(190deg,#e3a63b 0%,#b4652f 55%,#6b3a1f 100%)}
.note{font-size:.85rem;color:var(--muted);margin-top:14px}

/* area + reviews */
.split{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.towns{list-style:none;display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.towns li{background:var(--white);border:1px solid var(--sand);padding:8px 16px;border-radius:999px;font-weight:500}
.panel{background:var(--forest);color:#e6eee1;border-radius:var(--radius);padding:40px}
.panel h2{color:#fff;font-size:2rem;margin:8px 0 14px}
.stars{display:flex;gap:4px;color:#f2c56b;margin-bottom:10px}
.stars svg{fill:#f2c56b}
.placeholder{border:2px dashed rgba(255,255,255,.35);border-radius:12px;padding:20px;margin:20px 0;font-style:italic}

/* faq */
.faq{background:var(--white)}
.faq-list{max-width:780px}
details{border-bottom:1px solid var(--sand);padding:20px 0}
summary{font-weight:600;font-size:1.1rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;color:var(--forest)}
summary::after{content:"+";font-size:1.5rem;line-height:1;color:var(--leaf)}
details[open] summary::after{content:"–"}
details p{margin-top:10px;color:var(--muted)}

/* contact */
.contact .split{align-items:start}
.info{list-style:none;margin-top:24px;display:grid;gap:18px}
.info li{display:flex;gap:14px;align-items:center;font-size:1.05rem}
.info .ic{width:46px;height:46px;border-radius:50%;background:#e6efe0;color:var(--moss);display:grid;place-items:center;flex:none}
.info a{font-weight:600;text-decoration:none;color:var(--forest)}
form{background:var(--white);padding:34px;border-radius:var(--radius);box-shadow:var(--shadow);display:grid;gap:14px}
form h3{font-size:1.5rem}
.row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
label{font-size:.85rem;font-weight:600;color:var(--muted);display:grid;gap:6px}
input,select,textarea{font:inherit;padding:12px 14px;border:1px solid #d6d2c6;border-radius:10px;background:#fbfaf6}
input:focus,select:focus,textarea:focus{outline:2px solid var(--sage);border-color:transparent}
#form-msg{font-size:.95rem;color:var(--moss);font-weight:500}

footer{background:#16291d;color:#b9c6b4;padding:40px 0 90px;font-size:.9rem}
footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px}
footer b{color:#fff}

/* mobile call bar */
.callbar{display:none;position:fixed;left:0;right:0;bottom:0;z-index:30;background:#e3a63b;
         text-align:center;padding:14px;font-weight:700;text-decoration:none;color:#1b1f1c;
         box-shadow:0 -4px 16px rgba(0,0,0,.15)}

@media (max-width:900px){
  .grid{grid-template-columns:1fr 1fr}
  .steps{grid-template-columns:1fr 1fr}
  .split{grid-template-columns:1fr}
  .links a:not(.btn){display:none}
}
@media (max-width:620px){
  section{padding:64px 0}
  .topbar .hide-sm{display:none}
  .grid,.steps,.row{grid-template-columns:1fr}
  .gallery{grid-template-columns:1fr 1fr;grid-template-rows:180px 140px 140px}
  .shot:first-child{grid-column:span 2;grid-row:auto}
  .shot:last-child{grid-column:span 2}
  .links .btn{display:none}
  .hero .wrap{padding-top:70px;padding-bottom:120px}
  .callbar{display:flex;justify-content:center;gap:8px;align-items:center}
}
</style>
</head>
<body>

<div class="topbar"><div class="wrap">
  <span>$icon_pin Serving $town &amp; the South Coast</span>
  <span class="hide-sm">$icon_phone <a href="tel:$phone_digits">$phone</a></span>
</div></div>

<nav><div class="wrap">
  <a class="logo" href="#top">
    <span class="logo-mark">$icon_leaf</span>
    <span><b>$name</b><small>$tagline</small></span>
  </a>
  <div class="links">
    <a href="#services">Services</a><a href="#work">Our Work</a>
    <a href="#area">Service Area</a><a href="#faq">FAQ</a>
    <a class="btn btn-primary" href="#quote">Free Estimate</a>
  </div>
</div></nav>

<header class="hero" id="top">
  <svg class="hero-art" viewBox="0 0 1440 640" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
    <defs>
      <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#f6f2e9"/><stop offset="1" stop-color="#e3eedb"/>
      </linearGradient>
    </defs>
    <rect width="1440" height="640" fill="url(#sky)"/>
    <circle cx="1150" cy="170" r="90" fill="#f2c56b" opacity=".6"/>
    <circle cx="1150" cy="170" r="54" fill="#f2c56b" opacity=".35"/>
    <path d="M0 470 C240 400 420 430 640 455 S1100 380 1440 420 V640 H0Z" fill="#b9d3a5" opacity=".8"/>
    <path d="M0 530 C300 480 520 520 780 505 S1200 470 1440 500 V640 H0Z" fill="#5c8a4a"/>
    <path d="M0 590 C360 560 760 600 1080 575 S1340 570 1440 580 V640 H0Z" fill="#8fae7e"/>
    <g fill="#5c8a4a">
      <path d="M1010 470 l26 -90 26 90z"/><path d="M1052 480 l34 -120 34 120z"/>
      <path d="M1110 474 l24 -80 24 80z"/><path d="M1240 470 l30 -104 30 104z"/>
    </g>
    <g stroke="#a9c597" stroke-width="2" opacity=".5">
      <path d="M0 610 H1440"/><path d="M0 625 H1440"/>
    </g>
  </svg>
  <div class="wrap">
    <p class="eyebrow">$town &middot; Landscaping</p>
    <h1>A yard you&rsquo;re <em>proud</em> to come home to.</h1>
    <p class="lead">Lawn care, seasonal cleanups, planting and patios from a local South Coast crew. One call and it&rsquo;s handled.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="#quote">Get a Free Estimate</a>
      <a class="btn btn-ghost" href="tel:$phone_digits">$icon_phone Call $phone</a>
    </div>
    <ul class="promises">$promises</ul>
  </div>
</header>

<section id="services"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">What we do</p>
    <h2>Everything your property needs, season to season</h2>
    <p>From the first spring cleanup to the last leaf in November, $name keeps your yard in shape so you don&rsquo;t have to.</p>
  </div>
  <div class="grid">$services</div>
</div></section>

<section class="process"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">How it works</p>
    <h2>Simple from the first call</h2>
  </div>
  <ol class="steps">$steps</ol>
</div></section>

<section id="work"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Our work</p>
    <h2>Recent projects around the South Coast</h2>
  </div>
  <div class="gallery">$gallery</div>
  <p class="note">Project photos coming soon.</p>
</div></section>

<section id="area" class="process"><div class="wrap split">
  <div>
    <p class="eyebrow">Service area</p>
    <h2 style="font-size:clamp(1.9rem,3.6vw,2.7rem);margin:8px 0 12px">Based in North Dartmouth. Working all over the South Coast.</h2>
    <p style="color:var(--muted)">Not sure if you&rsquo;re in range? Give us a call at $phone.</p>
    <ul class="towns">$towns</ul>
  </div>
  <div class="panel">
    <div class="stars">$icon_star$icon_star$icon_star$icon_star$icon_star</div>
    <p class="eyebrow" style="color:#b8d3a6">Reviews</p>
    <h2>Happy with your yard?</h2>
    <div class="placeholder">[Add a real customer review here, with the customer&rsquo;s permission.]</div>
    <a class="btn btn-primary" href="$google_review_url">Leave us a Google review</a>
  </div>
</div></section>

<section id="faq" class="faq"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">FAQ</p>
    <h2>Common questions</h2>
  </div>
  <div class="faq-list">$faq</div>
</div></section>

<section id="quote" class="contact"><div class="wrap split">
  <div>
    <p class="eyebrow">Get in touch</p>
    <h2 style="font-size:clamp(1.9rem,3.6vw,2.7rem);margin:8px 0 12px">Request your free estimate</h2>
    <p style="color:var(--muted)">Tell us a little about the job and we&rsquo;ll get back to you. For the fastest answer, just call.</p>
    <ul class="info">
      <li><span class="ic">$icon_phone</span><div>Phone<br><a href="tel:$phone_digits">$phone</a></div></li>
      <li><span class="ic">$icon_pin</span><div>Location<br><b>$town</b></div></li>
      <li><span class="ic">$icon_clock</span><div>Hours<br><b>$hours</b></div></li>
    </ul>
  </div>
  <form id="quote-form" action="$form_endpoint" method="POST">
    <h3>Tell us about your yard</h3>
    <div class="row">
      <label>Name<input name="name" required></label>
      <label>Phone<input name="phone" type="tel" required></label>
    </div>
    <label>Street &amp; town<input name="address"></label>
    <label>Service needed<select name="service">$service_options<option>Something else</option></select></label>
    <label>Details<textarea name="details" rows="4" placeholder="Size of the yard, timing, anything else we should know"></textarea></label>
    <button class="btn btn-primary" type="submit">Send Request</button>
    <p id="form-msg" role="status"></p>
  </form>
</div></section>

<footer><div class="wrap">
  <div><b>$name $tagline</b><br>$town &middot; <a href="tel:$phone_digits">$phone</a></div>
  <div>&copy; $year $name $tagline</div>
</div></footer>

<a class="callbar" href="tel:$phone_digits">$icon_phone Call $phone</a>

<script>
// If no form endpoint is configured, don't pretend to send anything.
(function(){
  var f = document.getElementById('quote-form');
  if (!f.getAttribute('action')) {
    f.addEventListener('submit', function(e){
      e.preventDefault();
      document.getElementById('form-msg').textContent =
        'Online requests are coming soon. Please call $phone for now.';
    });
  }
})();
</script>
</body>
</html>
""")

# ─────────────────────────────────────────────────────────────────────────────
def build(c=CONFIG):
    from datetime import date
    return PAGE.substitute(
        name=escape(c["name"]), tagline=escape(c["tagline"]), town=escape(c["town"]),
        phone=escape(c["phone"]), phone_digits="+1" + "".join(ch for ch in c["phone"] if ch.isdigit()),
        hours=escape(c["hours"]), google_review_url=escape(c["google_review_url"]),
        form_endpoint=escape(c["form_endpoint"]), year=date.today().year,
        promises=build_promises(c), services=build_services(c), steps=build_steps(c),
        gallery=build_gallery(c), towns=build_towns(c), faq=build_faq(c),
        service_options=build_service_options(c),
        icon_pin=icon("pin", 16), icon_phone=icon("phone", 18), icon_leaf=icon("leaf", 22),
        icon_clock=icon("clock", 20), icon_star=icon("star", 22),
    )

if __name__ == "__main__":
    import sys
    import webbrowser

    if sys.version_info < (3, 6):
        print("This script needs Python 3.6 or newer. Download it from python.org.")
        input("Press Enter to close...")
        sys.exit(1)

    try:
        out = Path(__file__).resolve().with_name("index.html")
        out.write_text(build(), encoding="utf-8")
        print(f"Done! Website saved to:\n  {out}\n")
        print("Opening it in your web browser...")
        webbrowser.open(out.as_uri())          # shows the actual website
    except Exception as err:                   # show the error instead of vanishing
        print(f"Something went wrong:\n  {err}")

    # Keep the window open when the script is double-clicked on Windows/Mac
    if sys.stdin and sys.stdin.isatty():
        input("\nPress Enter to close this window...")
