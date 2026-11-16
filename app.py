#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 (NMDP) National Marrow Donor Program. All Rights Reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import connexion
from flask import redirect

# Create the Connexion application instance for Flask
connexion_app = connexion.FlaskApp(__name__, specification_dir="./")
connexion_app.add_api("api-spec.yaml")

# Expose ASGI app for uvicorn/gunicorn with uvicorn workers
app = connexion_app


@app.route("/")
def index():
    return redirect("/ui")


if __name__ == "__main__":
    # Run the application on port 8080
    connexion_app.run(port=8080)
