import pytest
from orderflow.orders import calculate_total, create_order


def test_total_local():
    assert calculate_total([{"product_id": 2, "quantity": 2}]) == 1950


def test_total_coupon():
    assert calculate_total([{"product_id": 1, "quantity": 1}], coupon="SAVE10") == 2580


def test_unknown_item():
    with pytest.raises(ValueError):
        calculate_total([{"product_id": 99, "quantity": 1}])


def test_create_order():
    assert create_order([{"product_id": 3, "quantity": 1}], "student@example.test")["total"] == 470
