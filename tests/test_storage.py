from orderflow.storage import connect_database, find_orders_by_email, save_order


def test_storage_roundtrip():
    with connect_database() as conn:
        save_order(conn, "student@example.test", 500)
        assert len(find_orders_by_email(conn, "student@example.test")) == 1
