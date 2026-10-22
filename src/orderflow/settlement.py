"""Daily settlement preparation from delivered orders."""
from collections import defaultdict
from datetime import datetime

def payments_for_settlement(records: list[dict], day: str):
    selected = []
    for record in records:
        paid_at = datetime.fromisoformat(record['paid_at'])
        if paid_at.strftime('%Y-%m-%d') == day and record['state'] == 'paid':
            selected.append(record)
    return selected

def sum_by_merchant(records: list[dict]) -> dict[int, int]:
    totals = defaultdict(int)
    for record in records:
        totals[int(record['merchant_id'])] += int(record['amount'])
    return dict(totals)

def reconcile(expected: list[dict], actual: list[dict]) -> list[dict]:
    """Find transactions with mismatched amounts."""
    actual_by_ref = {row['reference']: row for row in actual}
    differences = []
    for item in expected:
        match = actual_by_ref.get(item['reference'])
        if match is None or match['amount'] != item['amount']:
            differences.append({'reference': item['reference'],
                                'expected': item['amount'],
                                'actual': match['amount'] if match else None})
    return differences

def settlement_reference(merchant_id: int, day: str) -> str:
    return f'SET-{merchant_id}-{day.replace("-", "")}'
