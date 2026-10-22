"""Shipment preparation and carrier selection."""
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Mapping

ZONES = {'local': 1, 'regional': 2, 'remote': 3}
CARRIERS = {'parcel': 250, 'express': 520, 'economy': 170}

@dataclass(frozen=True)
class Shipment:
    tracking_code: str
    carrier: str
    planned_date: str
    price: int

def delivery_estimate(zone: str, carrier: str, weight_kg: float):
    if zone not in ZONES:
        raise ValueError('Unsupported zone')
    if carrier not in CARRIERS:
        raise ValueError('Unsupported carrier')
    if weight_kg <= 0 or weight_kg > 100:
        raise ValueError('Unsupported weight')
    base = CARRIERS[carrier]
    return base + ZONES[zone] * 80 + int(weight_kg * 24)

def prepare_shipment(order_id: int, zone: str, carrier: str, weight_kg: float, today=None):
    if today is None:
        today = date.today()
    price = delivery_estimate(zone, carrier, weight_kg)
    extra = {'express': 1, 'parcel': 3, 'economy': 5}[carrier]
    planned = today + timedelta(days=extra + ZONES[zone])
    return Shipment(f'OF-{order_id:06d}', carrier, planned.isoformat(), price)

def consolidate_shipments(shipments: list[Mapping]):
    groups = {}
    for shipment in shipments:
        key = (shipment['region'], shipment['carrier'])
        if key not in groups:
            groups[key] = {'packages': 0, 'weight': 0.0, 'fees': 0}
        groups[key]['packages'] += 1
        groups[key]['weight'] += float(shipment['weight'])
        groups[key]['fees'] += int(shipment['fee'])
    return groups
