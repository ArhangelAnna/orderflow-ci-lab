from orderflow.reporting import build_catalog_csv, report_totals, compact_report


def test_export():
    assert "Keyboard" in build_catalog_csv("electronics")
    assert "Mug" not in build_catalog_csv("electronics")


def test_report():
    items = [{"product_id": 2, "quantity": 2}]
    assert report_totals(items) == 1800
    assert compact_report(items) == "2:2;"
