import os
from flask import Flask, jsonify
from flask_cors import CORS
from tldr import TLDR

app = Flask(__name__)
CORS(app)

@app.route("/")
def health_check():
    return jsonify({'status': 'OK'})  

@app.route("/tldr/<string:query>", methods=["POST"])
def tldr(query: str):
    tldr = TLDR()
    summary = tldr.tldr(query)
    return jsonify({"TLDR": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(
        os.environ.get("PORT", 80)), threaded=True)