from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour Jerry 👋"


@app.route("/users")
def getUsers():
   return "All users!"


@app.route("/user/<int:userId>")
def getUser(userId):
    return f"User numero {userId}"


@app.route('/users', methods=['POST'])
def creer_utilisateur():
   return " utilisateur cree"



@app.route('/info')
def info():

    utilisateur = {
        "nom": "Jerry",
        "age": 15,
        "ville": "Yaoundé"
    }

    return jsonify(utilisateur)

app.run(debug=True)







if __name__ == "__main__":
    app.run(debug=True)


