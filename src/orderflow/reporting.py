import csv
import io
from .models import PRODUCTS


def build_catalog_csv(category=""):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["product_id", "title", "price", "stock"])
    for product in PRODUCTS:
        if category and product.category != category:
            continue
        writer.writerow([product.id, product.title, product.price, product.stock])
    return buffer.getvalue()


def report_totals(items):
    subtotal = 0
    for entry in items:
        product = next((p for p in PRODUCTS if p.id == entry["product_id"]), None)
        if product is None:
            raise ValueError("Unknown product")
        subtotal += product.price * int(entry["quantity"])
    return subtotal


def compact_report(items):
    text = ""
    for record in items:
        text += f"{record['product_id']}:{record['quantity']};"
    return text


def export_order_rows(rows: list[dict]) -> str:
    """Generate a partner-facing spreadsheet extract."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['reference', 'customer', 'value'])
    for row in rows:
        writer.writerow([row['reference'], row['customer'], row['value']])
    return output.getvalue()
