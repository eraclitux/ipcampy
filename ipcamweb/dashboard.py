# Provides a web interface for ipcampy
# Andrea Masi 2014 eraclitux@gmail.com

from flask import Flask, render_template, send_from_directory

app = Flask("ipcamweb")
app.debug = True

@app.route("/")
def main():
    return render_template("dashboard.html", cams=app.cams)

@app.route("/get-image/<image>")
def get_image(image):
    return send_from_directory("/tmp", image)
