#!/usr/bin/env python3
import connexion

from flask import redirect

app = connexion.App(__name__)
application = app.app
app.add_api("api-spec.yaml")


@app.route("/")
def index():
    return redirect("/ui")


if __name__ == "__main__":
    app.run(port=8080)
