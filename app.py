import os
from flask import Flask, request, abort

from project.utils import build_query

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query/", methods=["POST", "GET"])
def perform_query():

    """Getting parametres"""
    file_name = request.args.get('file_name')
    cmd1 = request.args.get('cmd1')
    value1 = request.args.get('value1')
    cmd2 = request.args.get('cmd2')
    value2 = request.args.get('value2')

    """Check if required fields are filled"""
    if not(cmd1 and value1 and file_name):
        abort(400)

    """Creating and checking file path"""
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400), "Filepath doesnt exist"

    """Manipulating with file"""
    try:
        with open(file_path) as file:
            res = build_query(cmd1, value1, file)
            if cmd2 and value2:
                res = build_query(cmd2, value2, res)
            res = "\n".join(res)
    except (ValueError, TypeError) as e:
        abort(400, e)

    return app.response_class(res, content_type="text/plain")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
