# Provides a web interface for ipcampy
# Andrea Masi 2014 eraclitux@gmail.com

import datetime
from flask import Flask, render_template, send_from_directory, redirect, session, request, url_for
from utils import list_snapshots_days, list_snapshots_hours, list_snapshots_for_a_minute

app = Flask("ipcamweb")
USERNAME = "watcher"

def is_authenticated():
    user = session.get('username') 
    paswd = session.get('password')
    if user == USERNAME and paswd == app.PASSWORD:
        is_authenticated = True
    else:
        is_authenticated = False
    return is_authenticated

@app.route("/")
def main():
    if is_authenticated():
        return render_template("main.html", cams=app.cams)
    else:
        return redirect(url_for('login'))

@app.route("/cam/<int:cam_index>")
def cam_detail(cam_index):
    days = list_snapshots_days(app.store_path, app.cams[cam_index - 1].cam_id)
    return render_template("cam_detail.html", cam_index=cam_index, days=days, cam=app.cams[cam_index - 1])

@app.route("/screenshots/<int:cam_index>/<day>")
def screenshots_details(cam_index, day):
    hours = list_snapshots_hours(app.store_path, app.cams[cam_index - 1].cam_id, day)
    return render_template(
            "screenshots_details.html", 
	    day=(datetime.datetime.strptime(day, "%d%m%Y").strftime('%d/%m/%y'), day),
            cam_index=cam_index, 
            hours=hours, 
            cam=app.cams[cam_index - 1],
    )

@app.route("/view-screenshots/<int:cam_index>/<day>/<hourm>")
def view_screenshots(cam_index, day, hourm):
    screenshots = list_snapshots_for_a_minute(
            app.store_path,
            app.cams[cam_index - 1].cam_id,
            day,
            hourm,
    )
    return render_template(
            "view_screenshots.html",
            cam_index=cam_index, 
            day=day,
	    date=datetime.datetime.strptime(day, "%d%m%Y").strftime('%d/%m/%y'),
            hourm=hourm,
            screenshots=screenshots,
            cam=app.cams[cam_index - 1],
    )

@app.route("/view-screenshot/<int:cam_index>/<day>/<hourm>/<screenshot>")
def view_screenshot(cam_index, day, hourm, screenshot):
    return render_template(
            "view_screenshot.html",
            cam_index=cam_index, 
            day=day,
            hourm=hourm,
            screenshot=screenshot,
            cam=app.cams[cam_index - 1],
    )

@app.route("/get-image/<int:cam_index>/<day>/<hour>/<image>")
def get_image(cam_index, image, day, hour):
    serve_path = app.store_path+"/"+app.cams[cam_index - 1].cam_id+"/"+day+"/"+hour
    return send_from_directory(serve_path, image)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if is_authenticated():
        return redirect(url_for('main'))
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if is_authenticated():
            return redirect(url_for('main'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))
