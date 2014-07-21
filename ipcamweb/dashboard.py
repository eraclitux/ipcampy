# Provides a web interface for ipcampy
# Andrea Masi 2014 eraclitux@gmail.com

from flask import Flask, render_template, send_from_directory, redirect, session, request, url_for

app = Flask("ipcamweb")
# FIXME
app.debug = True
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

@app.route("/cam/<int:cam_id>")
def cam_detail(cam_id):
    return render_template("cam_detail.html", cam=app.cams[cam_id-1])

# FIXME stub
@app.route("/get-image/<image>")
def get_image(image):
    return send_from_directory("/tmp", image)

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
