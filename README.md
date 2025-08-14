# Evidence Eye – Password Catcher (Flask)

A simple HTML5 Canvas + Flask + Jinja game where the player catches **strong passwords** and avoids **weak passwords**. Catching a weak password ends the game. Missing too many strong passwords also ends the game. After the game, an **After-Action Review** shows what you caught and quick tips.

## Tech Stack
- HTML5 + CSS (vanilla)
- Flask (Python)
- Jinja templates

## How to Run (Local)
1. Ensure Python 3.9+ is installed.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
4. Install Flask:
   ```bash
   pip install Flask
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open your browser at: http://127.0.0.1:5000/

## Customize Password Pools
Edit `STRONG_PASSWORDS` and `WEAK_PASSWORDS` in `app.py`. They are also shuffled each run for variety.

## Gameplay Notes
- **Controls:** Left/Right arrows or mouse to move the basket.
- **Goal:** Catch strong passwords only.
- **Fail Conditions:**
  - Catch a weak password → immediate game over.
  - Miss 5 strong passwords → game over.
- **Review:** A table shows everything you caught or missed, with verdicts and tips.

## Folder Structure
```
cybercase_password_catcher/
├─ app.py
├─ templates/
│  ├─ base.html
│  └─ index.html
└─ static/
   ├─ style.css
   └─ game.js
```

## Integration Tip (CyberCase Files)
Mount this route within your Evidence Eye section (e.g., at `/evidence/password-catcher`). You can also inject your own brand palette by editing `:root` CSS variables.
