from flask import Flask, jsonify, render_template, request
from costume import suggest_costume
import random

app = Flask(__name__)

# Home page (HTML form)
@app.route('/')
def home():
    return render_template("index.html")

# Single suggestion for a theme
@app.route('/costume/<theme>')
def costume(theme):
    suggestion = suggest_costume(theme)
    return jsonify({"theme": theme, "suggestion": suggestion})

# Multiple suggestions for a theme
@app.route('/costume/<theme>/all')
def costume_all(theme):
    suggestions = [suggest_costume(theme) for _ in range(3)]
    return jsonify({"theme": theme, "suggestions": suggestions})

# Random theme suggestion
@app.route('/costume/random')
def costume_random():
    themes = ["spooky", "funny", "default"]
    theme = random.choice(themes)
    suggestion = suggest_costume(theme)
    return jsonify({"theme": theme, "suggestion": suggestion})

# Optional: form submission
@app.route('/submit', methods=['POST'])
def submit():
    theme = request.form.get("theme")
    suggestion = suggest_costume(theme)
    return render_template("index.html", result=suggestion, theme=theme)

if __name__ == "__main__":
    app.run(debug=True)
