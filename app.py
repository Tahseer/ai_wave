from flask import Flask, render_template, request
from ai_engine import ask_ai, generate_pine_script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    parsed_data = None
    pine_script = None
    if request.method == "POST":
        user_prompt = request.form["user_prompt"]  # <-- this line is updated!
        try:
            data = ask_ai(user_prompt)
            parsed_data = data
            symbol = data["symbol"]
            timeframes = data["timeframes"]
            indicators = data["indicators"]
            pine_script = generate_pine_script(symbol, timeframes, indicators)
        except Exception as e:
            parsed_data = f"Error: {str(e)}"
    return render_template("index.html", parsed_data=parsed_data, pine_script=pine_script)

if __name__ == "__main__":
    app.run(debug=True)
