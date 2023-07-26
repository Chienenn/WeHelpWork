from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

USER_DATA = {"username": "test", "password": "test"}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        checkbox = request.form.get("checkbox")

        if checkbox == "on" and (not username or not password):
            error_message = "未輸入帳號或密碼"
            return redirect(url_for("error_page", message=error_message))

        elif (
            username != USER_DATA["username"] or password != USER_DATA["password"]
        ) and checkbox == "on":
            error_message = "帳號或密碼輸入錯誤"
            return redirect(url_for("error_page", message=error_message))

        elif (
            username == USER_DATA["username"]
            and password == USER_DATA["password"]
            and checkbox == "on"
        ):
            session["signed_in"] = True
            session.modified = True
            return redirect(url_for("success_page"))

    if session.get("signed_in"):
        return redirect(url_for("success_page"))
    else:
        return render_template("week4-2.html")


@app.route("/signin", methods=["POST"])
def verification_endpoint():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USER_DATA["username"] and password == USER_DATA["password"]:
        session["signed_in"] = True
        session.modified = True
        return redirect(url_for("success_page"))
    else:
        error_message = "帳號或密碼輸入錯誤"
        return redirect(url_for("error_page", message=error_message))


@app.route("/member")
def success_page():
    if not session.get("signed_in"):
        return redirect(url_for("home"))
    return render_template("success.html")


@app.route("/signout", methods=["GET"])
def signout():
    session["signed_in"] = False
    return redirect(url_for("home"))


@app.route("/error")
def error_page():
    error_message = request.args.get("message")
    return render_template("error.html", error_message=error_message)


@app.route("/square/<int:number>")
def square_number_page(number):
    squared_number = number * number
    return render_template(
        "squared_number.html", number=number, squared_number=int(squared_number)
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
