import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Gemini API
genai.configure(api_key=os.environ.get("AIzaSyAmFL6zI8lfXkf86eNTBDW2NhjgfO3Qyy8"))
model = genai.GenerativeModel("gemini-1.5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = model.generate_content(prompt=f"Answer in Malayalam, farmer-friendly: {user_msg}")
    reply_text = response.candidates[0].content[0].text if response.candidates else "Sorry!"
    return jsonify({"reply": reply_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)
