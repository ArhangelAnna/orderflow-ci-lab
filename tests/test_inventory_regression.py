
from orderflow.inventory import Warehouse, allocate_order, release_order


def test_duplicate_sku_cannot_overreserve():
    warehouse = Warehouse({"A": 5})

    result = allocate_order(
        warehouse,
        "ORD-1",
        [
            {"sku": "A", "quantity": 4},
            {"sku": "A", "quantity": 4},
        ],
    )

    assert result is False
    assert warehouse.available["A"] == 5
    assert "ORD-1" not in warehouse.reserved


def test_repeated_reservation_does_not_lose_stock():
    warehouse = Warehouse({"A": 5})

    first_result = allocate_order(
        warehouse,
        "ORD-1",
        [{"sku": "A", "quantity": 2}],
    )

    second_result = allocate_order(
        warehouse,
        "ORD-1",
        [{"sku": "A", "quantity": 1}],
    )

    assert first_result is True
    assert second_result is False

    assert warehouse.available["A"] == 3
    assert warehouse.reserved["ORD-1"] == {"A": 2}

    release_order(warehouse, "ORD-1")

    assert warehouse.available["A"] == 5
    assert "ORD-1" not in warehouse.reserved
