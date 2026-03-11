from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/user/<username>/<int:age>")
def user(username,age):
    if username.isdigit() or age < 18:
        return "Invalid details. Enter a valid username and age.!"
    return f"Welcome to flask... {username}!. Your age is {age} years!"
@app.route("/profile/<username>")
def profile(username):
    return f"Welcome to {username.upper()}'s profile!"
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form['password']
        return redirect(url_for("index"))
    return render_template("login.html")
@app.route("/api/data", methods=["POST"])
def data():
    username = request.form["username"]
    password = request.form["password"]

    return {"name": username, "password": password}
if __name__ == "__main__":
    app.run(debug=True)

