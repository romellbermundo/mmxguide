# ⚡ Mega Man X Field Guide

<div align="center">

**YOUR MISSION. YOUR ROUTE. YOUR POCKET GUIDE.**

*A fast, focused companion for the Maverick hunt.*

[🌐 Open the Live Field Guide](https://romellbermundo.github.io/mmxguide/) · [📦 Source Code](https://github.com/romellbermundo/mmxguide)

![GitHub Pages](https://img.shields.io/badge/Hosting-GitHub%20Pages-238636) ![HTML](https://img.shields.io/badge/Built%20with-HTML%20%26%20CSS-1769aa) ![Mobile First](https://img.shields.io/badge/Design-Mobile--First-00a6b2) ![Version](https://img.shields.io/badge/Version-1.5.1-64748b)

</div>

---

## 📑 Table of Contents

- [About the Field Guide](#-about-the-field-guide)
- [How It Works](#-how-it-works)
- [Key Features](#-key-features)
- [Getting Started](#-getting-started)
- [Publishing on GitHub Pages](#-publishing-on-github-pages)
- [Project Structure](#-project-structure)
- [Technology](#-technology)
- [Design Philosophy](#-design-philosophy)
- [Limitations and Game Notes](#-limitations-and-game-notes)
- [Credits](#-credits)
- [Version History](#-version-history)

---

## 📖 About the Field Guide

**Spend less time searching for answers and more time playing.**

The **Mega Man X Field Guide** is a compact, mobile-first reference for *Mega Man X* (1993). It groups the eight Maverick weaknesses, four armor upgrades, and four Sub-Tanks by stage, with a few useful SNES secrets at the bottom.

Built to be checked between stages, the guide favors immediate answers over long walkthroughs. No accounts, downloads, ads, or navigation through multiple pages are required.

The selector shows **X1–X8**, but **only X1 currently has guide content**. The remaining entries are intentionally disabled placeholders.

---

## 🔄 How It Works

```text
OPEN THE FIELD GUIDE
         │
         ▼
     SELECT X1
         │
         ▼
   FIND WHAT YOU NEED
         │
    ┌────┼────────┬─────────┐
    ▼    ▼        ▼         ▼
 BOSSES  ARMOR   SUB-TANKS  SECRETS
    │    │        │         │
    └────┴────────┴─────────┘
         │
         ▼
   RETURN TO THE GAME
```

The guide is a single static HTML file with embedded CSS. Information is grouped into eight stage cards, without menus, server requests, or application state to manage.

---

## ✨ Key Features

### 🎯 Eight Maverick Stage Cards

See a suggested boss order, each Maverick's weakness, and the collectibles in that stage in one place. **Chill Penguin** is the recommended first fight using the X-Buster.

### 🛡️ Four Armor Capsules

Find the **Legs, Helmet, Body, and Arms** upgrades with short stage-specific location hints.

### 🔋 Four Sub-Tanks

Locate the four Sub-Tanks in **Storm Eagle, Flame Mammoth, Armored Armadillo, and Spark Mandrill** stages.

### 🔐 Cheats & Secrets

Find the original SNES Sub-Tank password and an extra-life farming tip below the Maverick stage cards.

### 📱 Mobile-First Layout

A compact two-column stage-card layout keeps each boss and its collectibles together on phones and wider screens. The page is optimized for quick reference, although a single-screen fit cannot be guaranteed on every device.

### ⚡ Lightweight and Instant

No JavaScript framework, backend, login, or build tooling. Just HTML, CSS, and a locally hosted WebP sprite sheet.

### 🕹️ Series Selector

X1–X8 are visible for future expansion. **X2–X8 are disabled** and do not contain playable guides or reference data yet.

---

## 🚀 Getting Started

### Option A — Use the website

Visit **[Mega Man X Field Guide](https://romellbermundo.github.io/mmxguide/)** in your browser. No installation is required.

### Option B — Run locally

```bash
git clone https://github.com/romellbermundo/mmxguide.git
cd mmxguide
```

Open `index.html` in a browser. There are no packages to install or build commands to run.

---

## 🌐 Publishing on GitHub Pages

The project is designed for static hosting at:

**https://romellbermundo.github.io/mmxguide/**

To configure GitHub Pages:

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, select your preferred source: **GitHub Actions** or **Deploy from a branch**.
3. If using **GitHub Actions**, the included `.github/workflows/deploy.yml` publishes the static site; check the **Actions** tab for a successful run.
4. If using **Deploy from a branch**, select `main` and the repository root (`/root`).
5. Open the live URL after publishing completes.

**Deployment note:** The repository includes a GitHub Actions workflow at `.github/workflows/deploy.yml`. It deploys on pushes to `main` or when run manually. The guide requires no compilation.

---

## 🏗️ Project Structure

```text
mmxguide/
├── .github/workflows/deploy.yml  # Automatic Pages deployment
├── index.html                   # Content, layout, and embedded styles
├── mmxguide-snes-sprites.webp   # SNES-style portrait and item sprite sheet
└── README.md                    # Documentation and release history
```

Keeping the guide self-contained makes it easy to maintain, publish, and archive.

---

## 🛠️ Technology

| Layer | Technology |
|---|---|
| Structure | HTML5 |
| Styling | CSS3 |
| Layout | CSS Grid and responsive media queries |
| Hosting | GitHub Pages |
| Deployment | GitHub Actions |
| Version control | Git and GitHub |
| Build system | None required |
| Dependencies | One local WebP sprite sheet |

---

## 🎨 Design Philosophy

**A field guide should never interrupt the mission.**

The interface borrows its mood from classic science-fiction action games: alternating blue mission panels, cyan highlights, metallic borders, compact typography, and clear visual groupings.

- **Speed over complexity:** The information is immediately visible.
- **Mobile first:** Designed to consult while playing on another screen.
- **Useful density:** Short hints replace lengthy walkthroughs.
- **No unnecessary features:** No accounts, trackers, or elaborate navigation.
- **Expandable foundation:** Additional games can be introduced when their guides are ready.

*Small enough to stay out of the way. Useful enough to keep open.*

---

## 🔒 Limitations and Game Notes

- **X1 only:** X2–X8 are placeholders, not complete guides.
- **No Heart Tank section:** Intentionally excluded from this compact reference.
- **SNES-specific cheat:** The password targets the original SNES release and may not work in every port or collection.
- **Backtracking:** Some upgrades require revisiting stages with abilities obtained later.
- **Screen size:** Compact does not mean guaranteed zero scrolling.
- **Unofficial fan project:** Not affiliated with or endorsed by Capcom.

---

## 🙏 Credits

**Mega Man X** and its characters belong to **Capcom**. This independent, unofficial reference is intended for fans.

**Guide implementation and project development:** Romell Bermundo.

---

## 🏷️ Version History

### v1.5.1 — Alternating row colors

- Corrected the Maverick card palette to alternate by row instead of by column.
- Each horizontal pair now shares the same panel color, alternating blue and violet-blue down the guide.

### v1.5.0 — Compact mobile dashboard

- Reduced stage card height, sprite dimensions, padding, and section spacing to minimize scrolling.
- Kept two-column Maverick cards, readable text, alternating futuristic panel colors, and cheats at the bottom.
- Maintained responsive sizing for narrow phones and larger screens.

### v1.4.0 — Futuristic mission panels

- Moved Cheats & Secrets beneath the eight Maverick stage cards.
- Improved the fit and scale of armor, Sub-Tank, and cheat sprites.
- Introduced alternating blue stage-card backgrounds with clearer contrast from the page.
- Added subtle cyan console lighting and metallic borders while preserving the compact two-column mobile layout.

### v1.3.0 — Stage-by-stage guide

- Consolidated boss weaknesses, armor upgrades, and Sub-Tanks into eight Maverick stage cards.
- Placed each collectible's location hint directly beneath the corresponding boss.
- Preserved cheats, SNES-style sprites, recommended boss order, and mobile-first layout.

### v1.2.2 — SNES-style artwork

- Added pixel-art portraits to all eight Maverick weakness cards.
- Added armor, Sub-Tank, and cheat icons using the uploaded WebP sprite sheet.
- Kept the single-page mobile layout and existing gameplay reference content.

### v1.2.1 — Automatic GitHub Pages deployment

- Added GitHub Actions workflow to deploy the static site on pushes to `main` or manual runs.
- Updated deployment instructions and project structure to match the repository.

### v1.2.0 — Portfolio README and GitHub Pages reference

- Rebuilt the README following the NEXUS 01 documentation structure.
- Added prominent live-site and repository links, technology badges, and a table of contents.
- Documented the guide's features, architecture, deployment options, design principles, and limitations.
- Preserved the existing X1 website without modifying gameplay reference content.

### v1.1 — Compact X1 pocket guide

- Extended selector to X1–X8 while keeping X2–X8 disabled.
- Added cheats and secrets at the top, including the four Sub-Tanks password.
- Added all four Sub-Tank locations.
- Preserved eight Maverick weaknesses and four armor locations.
- Removed any mention of collecting Heart Tanks as guide content.
- Tightened spacing for a compact, mobile-first page.

### v1.0 — Mega Man X1 guide

- Added X1–X4 tabs with X1 active.
- Added eight Maverick bosses, recommended order, and weapon weaknesses.
- Added four armor upgrade locations.
- Created a responsive, dark-blue game-inspired layout.
