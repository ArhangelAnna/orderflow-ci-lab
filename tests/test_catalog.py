from orderflow.catalog import search_products, inventory_summary


def test_search():
    assert [p.title for p in search_products("mouse")] == ["Mouse"]


def test_sort():
    prices = [p.price for p in search_products(sort_by="price")]
    assert prices == sorted(prices)


def test_inventory():
    assert inventory_summary()["office"]["count"] == 2
