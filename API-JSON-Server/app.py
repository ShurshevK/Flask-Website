from flask import Flask
from mock_data import lists, list_items, abort


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return 'Hello world!'

@app.route("/lists", methods=['GET'])
def get_lists():
    return jsonify({'lists': lists})

@app.route("/lists/<int:list_id>", methods=['GET'])
def get_list(list_id):
    _list = [_list for _list in lists if _list['id'] == list_id][0]
    _items = [_item for _item in list_items if _item['list_id'] == list_id]
    if len(_items) > 0:
        _list['list_items'] = _items
    return jsonify({'list': _list})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '404 Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True)