# Spooky Hackathon Project

## About
Python Flask app to suggest Halloween costumes using Kiro.

## Running Locally
1. Clone repo
2. Create virtual environment: `python -m venv venv`
3. Activate venv:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run app: `python app.py`
6. Visit: http://127.0.0.1:5000

## Endpoints
- `/costume/<theme>` → Single costume suggestion
- `/costume/<theme>/all` → Multiple suggestions
- `/costume/random` → Random theme
- `/submit` → HTML form for interactive selection

## How Kiro was used
- Generated `costume.py` function
- Created `.spec` file for reproducibility
- Saved prompt in `.kiro/prompts.txt`

## Demo Video
[Insert YouTube/Vimeo link]

## Public URL
[Insert deployed app URL]
