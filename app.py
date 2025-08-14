from flask import Flask, render_template
import random

app = Flask(__name__)

# Strong and weak password pools (extendable)
STRONG_PASSWORDS = [
    "J@ck_2025!", "A9!rT_3k#Z", "M3ena$2048", "S!lver_F0x88", "Kite#Wind_77",
    "C0bAlt!_Nine", "Aur0ra@Sun*", "N!ght_Owl#39", "R1ver$Flow_09", "H@wk-Eye_55",
    "Xy!_93vK#2", "G@laxy-R1ngs_7", "Pyth0n@Flask!", "Djang0_R0cks#", "C0d3C@se_!2",
    "Str0ng&P@ss_01", "Trail#Bl@ze_66", "M00n_L@ke!5", "Gh0st$Guard_33", "S@feK#ey_90"
]

WEAK_PASSWORDS = [
    "12345", "password", "qwerty", "111111", "abc123",
    "iloveyou", "admin", "letmein", "welcome", "sunshine",
    "dragon", "football", "monkey", "login", "princess",
    "qwerty123", "1q2w3e", "000000", "passw0rd", "user"
]

@app.route("/")
def index():
    # Shuffle so each run feels fresh (data injected via Jinja)
    strong = STRONG_PASSWORDS[:]
    weak = WEAK_PASSWORDS[:]
    random.shuffle(strong)
    random.shuffle(weak)
    return render_template(
        "index.html",
        strong_passwords=strong,
        weak_passwords=weak
    )

if __name__ == "__main__":
    app.run(debug=True)
