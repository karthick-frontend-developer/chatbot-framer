from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 🔑 Gemini API Key
genai.configure(api_key="AIzaSyAmFL6zI8lfXkf86eNTBDW2NhjgfO3Qyy8")
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # Generate AI answer (local language friendly)
    ai_response = model.generate_content(
        f"Answer in Malayalam in simple farmer-friendly words. Question: {user_msg}"
    )

    return jsonify({"reply": ai_response.text})

if __name__ == "__main__":
    app.run(debug=True)
