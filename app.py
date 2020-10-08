from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "<H1>El lab de ipc1 sale en vacas</H1>"


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)