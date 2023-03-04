import os

from flask import Flask, request, abort

from utils import build_file

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST", "GET"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    cmd_1 = request.args.get('cmd_1')
    val_1 = request.args.get('val_1')
    cmd_2 = request.args.get('cmd_2')
    val_2 = request.args.get('val_2')
    file_name = request.args.get('file_name')

    if not(cmd_1 and val_1 and file_name):
        abort (404)

    file_path = os.path.join(DATA_DIR, file_name)
    if os.path.exists(file_path): # Проверка наличия данного пути
        abort(404)

    with open(file_path + '.txt') as file:
        res = build_file(cmd_1, val_1, file)
        if cmd_2 and val_2:
            result = build_file(cmd_2, val_2, res)
        res = '\n'.join(result)
    return app.response_class(res, content_type="text/plain")

if __name__ == '__main__':
    app.run(debug=True)