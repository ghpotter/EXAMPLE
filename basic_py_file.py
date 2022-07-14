from flask import Flask

import os
import hello, world

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>{}, {}!</p>".format(hello.get_hello(), world.get_world())


def main() -> None:
    print("{} {}".format(hello.get_hello(), world.get_world()))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)