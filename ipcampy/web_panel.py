from flask import Flask

app = Flask("ipcampy")

@app.route("/")
def main():
    return "Hi!"
