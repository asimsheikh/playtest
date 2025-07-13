from flask import Flask

app = Flask(__name__)
rt = app.route

with open("templates/index.html", "r") as f:
    index_html = f.read()


@rt("/")
def index():
    return index_html


if __name__ == "__main__":
    app.run(port=5000, debug=True)
