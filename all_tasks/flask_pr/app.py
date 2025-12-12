from flask import Flask, render_template, request, redirect
import sqlite3, os

app = Flask(__name__)

def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        conn.commit()
        conn.close()

init_db()
@app.route("/")
def home():
    return redirect("/signup")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?,?)",
                      (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "username already exists"
        conn.close()
        return "Signup successful! <a href='/login'>Go to login</a>"

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            return "Login successful!"
        else:
            return "Invalid username or password"

    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
