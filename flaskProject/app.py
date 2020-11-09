#Yüklü değilse önce Flask package yükleyin
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route("/<string:isim>")
def baslangic_api(isim: str):
    #isim = request.args.get("isim")
    return jsonify(data = isim),200

if __name__ == "__main__":
    app.run()