# Beam Deflection Calculator

A simple, browser-based tool to calculate maximum beam deflection under a point load — built for mechanical/civil engineering students and practitioners.

## What It Does
Enter beam type, load, length, material stiffness (Young's Modulus), and cross-section stiffness (Moment of Inertia) — get instant maximum deflection in millimeters.

## Supported Beam Types
- **Simply Supported** (load at center): `y_max = PL³ / (48EI)`
- **Cantilever** (load at free end): `y_max = PL³ / (3EI)`

## Tech Stack
Pure HTML + CSS + JavaScript. No frameworks, no build step, no API keys — runs entirely in the browser.

## How to Use
1. Open `index.html` in any browser (or visit the live GitHub Pages link below)
2. Select beam type
3. Enter load (N), length (m), Young's Modulus (GPa), and Moment of Inertia (mm⁴)
4. Tap "Calculate Deflection"

## Common Values for Reference
| Material | Young's Modulus (E) |
|---|---|
| Steel | ~200 GPa |
| Aluminum | ~69 GPa |
| Cast Iron | ~170 GPa |

## Deploying
This is a static site — works directly on **GitHub Pages** (no server needed, unlike the AI Hub projects):
1. Repo → Settings → Pages
2. Source: "Deploy from a branch" → `main` → `/ (root)`
3. Save — your calculator goes live at `https://<username>.github.io/<repo-name>/`

## Roadmap
- [ ] Add distributed load calculations (not just point load)
- [ ] Add beam deflection diagram/visualization
- [ ] Add stress and bending moment calculators

## Author
Harpreet Singh
