from flask import Flask, render_template, request, redirect, url_for, session, jsonify


app = Flask(__name__)
app.secret_key = "secret_key11"
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123123",
    "database": "website",
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    name = request.form.get("name")
    password = request.form.get("password")

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    check_query = "SELECT * FROM member WHERE username = %s"
    cursor.execute(check_query, (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        conn.close()
        return redirect(url_for("error_page", message="帳號已被註冊!"))

    insert_query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, username, password))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("signname")
    password = request.form.get("signpassword")

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT * FROM member WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        session["username"] = username
        cursor.close()
        conn.close()
        return redirect(url_for("member"))
    else:
        cursor.close()
        conn.close()
        return redirect(url_for("error_page", message="帳號或密碼輸入錯誤"))


@app.route("/member")
def member():
    if "username" not in session:
        return redirect(url_for("home"))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if "username" in session:
        username = session["username"]

        query = "SELECT id,name FROM member WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            user_name = user[1]
            query_messages = "SELECT msg.id, m.name, msg.content FROM member m JOIN message msg ON m.id = msg.member_id ORDER BY msg.time DESC"
            cursor.execute(query_messages)
            messages = cursor.fetchall()

    cursor.close()
    conn.close()

    if user:
        return render_template(
            "success.html", user_name=user_name, user_id=user_id, messages=messages
        )
    else:
        return redirect(url_for("home"))


@app.route("/createMessage", methods=["POST"])
def create_message():
    if "username" not in session:
        return redirect(url_for("home"))

    username = session["username"]

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT id FROM member WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        user_id = user[0]
        message_content = request.form.get("message")

        if message_content:
            message_query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
            cursor.execute(message_query, (user_id, message_content))
            conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("member"))


@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    message_id = request.args.get("message_id")
    if message_id is None:
        return jsonify({"success": False, "error": "Missing message_id"})

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT member_id FROM message WHERE id = %s", (message_id,))
    result = cursor.fetchone()

    if result:
        delete_query = "DELETE FROM message WHERE id = %s"
        cursor.execute(delete_query, (message_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True})

    else:
        cursor.close()
        conn.close()
        return jsonify({"success": False, "error": "Message not found"})


@app.route("/error")
def error_page():
    error_message = request.args.get("message")
    return render_template("error.html", error_message=error_message)


@app.route("/signout")
def signout():
    if "username" in session:
        session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
