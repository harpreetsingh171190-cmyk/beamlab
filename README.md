📐 Beam Deflection Calculator
� � �
A simple, browser-based tool to calculate maximum beam deflection under a point load — built for mechanical/civil engineering students and practitioners.
🔗 Live Demo: https://harpreetsingh171190-cmyk.github.io/beam-deflection-calculator/
�
�

Table of Contents
Features
Supported Beam Types
Tech Stack
How to Use
Reference Values
Run Locally
Roadmap
Features
⚡ Instant calculation, no page reload
📱 Mobile-friendly, responsive layout
🔒 Runs 100% client-side — no data leaves your browser
🎯 Two beam configurations supported out of the box
Supported Beam Types
Type
Formula
Simply Supported (load at center)
y_max = PL³ / (48EI)
Cantilever (load at free end)
y_max = PL³ / (3EI)
Tech Stack
Pure HTML + CSS + JavaScript. No frameworks, no build step, no API keys — runs entirely in the browser.
How to Use
Open the live demo — no installation needed
Select beam type
Enter load (N), length (m), Young's Modulus (GPa), and Moment of Inertia (mm⁴)
Tap Calculate Deflection
Common Values for Reference
Material
Young's Modulus (E)
Steel
~200 GPa
Aluminum
~69 GPa
Cast Iron
~170 GPa
Run Locally
git clone https://github.com/harpreetsingh171190-cmyk/beam-deflection-calculator.git
cd beam-deflection-calculator
# just open index.html in your browser — no build step needed
Roadmap
[ ] Add distributed load calculations (not just point load)
[ ] Add beam deflection diagram/visualization
[ ] Add stress and bending moment calculators
[ ] Add unit toggle (SI / Imperial)
Contributing
Issues and pull requests are welcome — feel free to suggest new beam types or calculators.
License
This project is licensed under the MIT License — free to use, modify, and share.
Author
Harpreet Singh — M.Tech (Mechanical Engineering) GitHub
