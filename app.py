import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# ✅ Correct way to configure Gemini API
genai.configure(api_key=os.environ.get("AIzaSyDhz17qnglpcViBiHljx1EnvEd9t2tnXuY"))
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    try:
        ai_response = model.generate_content(
            prompt=f"Answer in Malayalam in simple farmer-friendly words: {user_msg}"
        )
        reply = ai_response.candidates[0].content[0].text if ai_response.candidates else "⚠️ AI error"
    except Exception as e:
        reply = "⚠️ AI service error"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
