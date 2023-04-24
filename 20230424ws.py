
from flask import Flask, jsonify, request

app=Flask(__name__)

# dane= {
#     "imie": "Andrzej",
#     "nazwisko": "K",
#     "wiek": 33
# }

@app.route("/data.json")
def getAllJson():
    # return dane
    return jsonify(imie="Andrzej", nazwisko="Kos", wiek=33)

@app.route("/data.json", methods=['POST'])
def post():
    odebrane=request.json
    print(odebrane)
    return ""


if __name__ == "__main__":
    app.run(debug=True, port= 80)