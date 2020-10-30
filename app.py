from flask import Flask, redirect, url_for, request, render_template
import math, time
from log2db import logs


z = 0
app = Flask(__name__)
app.config["DEBUG"] = False


def refresh():
    l = logs()
    total, blocked, qt1, forwrd, locally, blacklists1 = l.convert()
    percent = math.ceil((int(blocked[0]) / int(total[0])) * 100)
    # l.close()
    return total, blocked, qt1, forwrd, locally, blacklists1, percent

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if (
            request.form["username"] != "Adgu@rd"
            or request.form["password"] != "Adgu@rd123"
        ):
            error = "Invalid Credentials. Please try again."
        else:
            global z
            z = 1
            return redirect(url_for("hello"))
    return render_template("login.html", error=error)


@app.route("/stats", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        if request.form["logout"] == "logout":
            return redirect(url_for("login"))
    else:
        if z != 1:
            return redirect(url_for("login"))
        total, blocked, qt1, forwrd, locally, blacklists1, percent = refresh()

        return render_template(
            "content.html",
            title="DnsMasq AdBlocker | Admin Panel",
            allQueries=total[0],
            blockedQueries=blocked[0],
            percent=percent,
            querytype=qt1,
            forwarded=forwrd,
            blacklists1=blacklists1,
            locally=locally,
        )


if __name__ == "main":
    app.run(host="0.0.0.0")


