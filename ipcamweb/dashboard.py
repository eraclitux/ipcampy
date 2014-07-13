# Provides a web interface for ipcampy
# Andrea Masi 2014 eraclitux@gmail.com

from flask import Flask, render_template, send_from_directory

app = Flask("ipcamweb")
app.debug = True

@app.route("/")
def main():
    return render_template("main.html", cams=app.cams)

@app.route("/cam/<int:cam_id>")
def cam_detail(cam_id):
    return render_template("cam_detail.html", cam=app.cams[cam_id-1])

@app.route("/get-image/<image>")
def get_image(image):
    return send_from_directory("/tmp", image)
