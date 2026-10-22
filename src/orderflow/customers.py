"""Customer segmentation and export policies."""
import csv
import io
from dataclasses import dataclass

@dataclass
class Customer:
    user_id: int
    email: str
    region: str
    lifetime_spend: int
    enabled: bool = True

def segment(customers: list[Customer], lower_bound: int, region: str = ''):
    return [c for c in customers if c.enabled and c.lifetime_spend >= lower_bound
            and (not region or c.region == region)]

def customer_export(customers: list[Customer]) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'email', 'region', 'lifetime_spend'])
    for customer in customers:
        writer.writerow([customer.user_id, customer.email, customer.region,
                         customer.lifetime_spend])
    return output.getvalue()

def rank_customers(customers: list[Customer], top: int = 10):
    return sorted(customers, key=lambda customer: customer.lifetime_spend,
                  reverse=True)[:top]
