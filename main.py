import config
from datetime import timedelta
from flask import Flask, render_template


# Инцилизация приложения Flask #

app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.permanent_session_lifetime = timedelta(days=365)





@app.route("/")
def login():
    return render_template("login.html")













if __name__ == "__main__":
    app.run(debug=True, port=8000)