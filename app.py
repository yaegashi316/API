from flask import Flask, jsonify, request
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def html():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post():
    animal = request.form["animal"]
    if animal == "cat":
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        # urlを受け取る
        res = response.json()
        # jsonで
        photo = res[0]["url"]
        # 配列？
    elif animal == "dog":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        res = response.json()
        photo = res["message"]
    else:
        response = requests.get("https://randomfox.ca/floof/")
        res = response.json()
        photo = res["image"]

    return render_template("post.html", photo=photo)

    # photo=
    # return response.json()


# @app.post("/post")
# def post():
#     print(request.json)
#     data = "OK"
#     return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

# response_cat = requests.get("https://api.thecatapi.com/v1/images/search")
# response_dog = requests.get("https://dog.ceo/api/breeds/image/random")
# response_fox = requests.get("https://randomfox.ca//images//56.jpg")


# result = response.text
# print(result)

# if __name__ == "__main__":
# app.run(host="127.0.0.1", port=8000, debug=True)
