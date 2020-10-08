from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "<H1>Está página fue modificada con un commit en consola</H1>"


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)