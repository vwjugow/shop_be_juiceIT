from project import create_app
from project.models import ShopItem, db
import json


def test_root():
    flask_app = create_app("envs/flask_test.cfg")
    with flask_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        assert b'{"message": "hola"}' == response.data


def test_create_item():
    flask_app = create_app("envs/flask_test.cfg")
    with flask_app.test_client() as test_client:
        items = ShopItem.query.filter_by(id=1).all()
        assert len(items) == 0
        response = test_client.post(
            "/shopitem",
            data=json.dumps(
                dict(
                    {
                        "name": "Slicker Jacket",
                        "description": "Wind and rain",
                        "image_url": "https://hplussport.com/wp-content/slicker-jacket_LYNDA_29941.jpg",
                        "price": 125.24,
                        "image_title": "title",
                    }
                )
            ),
            content_type="application/json",
        )
        assert response.status_code == 201
        items = ShopItem.query.filter_by(id=1).all()
        assert len(items) == 1
        item = items[0]
        assert 125.24 == item.price
        assert "Wind and rain" == item.description
        assert "Slicker Jacket" == item.name
        assert "title" == item.image_title
        assert (
            "https://hplussport.com/wp-content/slicker-jacket_LYNDA_29941.jpg"
            == item.image_url
        )
        db.session.delete(item)
        db.session.commit()
