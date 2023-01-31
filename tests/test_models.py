from project.models import ShopItem


def test_new_shop_item():
    item = ShopItem("name", 123.45, "desc", None, None)
    assert item.name == "name"
    assert item.description == "desc"
    assert item.price == 123.45
