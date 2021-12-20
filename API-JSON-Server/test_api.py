import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_json_with_proper_mimetype(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_hello_world(client):
    response = client.get('/')
    json = response.get_json()
    assert json['message'] == 'Hello world!'

def test_lists(client):
    response = client.get('/lists')
    json = response.get_json()
    assert len(json['lists']) == 2

def test_single_list(client):
    response = client.get('/lists/1')
    json = response.get_json()
    assert json['list']['name'] == 'This is an example list'

def test_single_list_items(client):
    response = client.get('/lists/1')
    json = response.get_json()
    assert len(json['list']['list_items']) == 3

def test_not_found(client):
    response = client.get('/not/real/url')
    json = response.get_json()
    assert response.status_code == 404
    assert json['error'] == '404 Not Found'

def get_list(list_id):
    _list = {}
    search = [_list for _list in lists if _list['id'] == list_id]
    if len(search) > 0:
        _list = search[0]
    else:
        abort(404)
    _items = [_item for _item in list_items if _item['list_id'] == list_id]
    if len(_items) > 0:
        _list['list_items'] = _items
    return jsonify({'list': _list})

def test_list_not_found(client):
    response = client.get('/lists/99')
    json = response.get_json()
    assert response.status_code == 404
    assert json['error'] == '404 Not Found'