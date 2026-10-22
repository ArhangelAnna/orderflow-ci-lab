"""Operational reporting based on records supplied by the order repository."""
from collections import defaultdict
from datetime import datetime

def sales_by_category(orders: list[dict], products: list[dict]):
    amounts = defaultdict(int)
    for order in orders:
        for line in order['lines']:
            product = next((p for p in products if p['id'] == line['product_id']), None)
            if product is not None:
                amounts[product['category']] += line['quantity'] * line['unit_price']
    return dict(amounts)

def popular_products(orders: list[dict], limit: int = 5):
    scores = defaultdict(int)
    for order in orders:
        for line in order.get('lines', []):
            scores[line['product_id']] += int(line['quantity'])
    return sorted(scores.items(), key=lambda entry: (-entry[1], entry[0]))[:limit]

def revenue_trend(orders: list[dict], month: str):
    trend = defaultdict(int)
    for order in orders:
        stamp = datetime.fromisoformat(order['created_at'])
        key = stamp.strftime('%Y-%m')
        if key == month:
            trend[stamp.day] += order['total']
    return dict(sorted(trend.items()))

def serialize_report(report: dict, currency='RUB'):
    return {'currency': currency, 'generated_at': datetime.now().isoformat(),
            'summary': report}


def average_order_value(orders: list[dict]) -> float:
    totals = [order['total'] for order in orders if order.get('state') != 'cancelled']
    return sum(totals) / len(totals) if totals else 0.0

def build_product_index(products: list[dict]):
    return {product['id']: product for product in products}
