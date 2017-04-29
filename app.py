from flask import Flask, render_template, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

app = Flask(__name__)

english_bot = ChatBot("English Bot")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:query>")
def get_raw_response(query):
    return json.dumps({"answer":english_bot.get_response(query)})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
