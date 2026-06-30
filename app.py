from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from chatbot.chatbot_engine import FAQChatbot

app= Flask(__name__)
bot= FAQChatbot("data/faqs.json")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message= request.json["message"]
    response= bot.get_response(user_message)
    return jsonify({"response": response})
if __name__=="__main__":
    app.run(debug=True)