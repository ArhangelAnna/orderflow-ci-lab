"""Warehouse state transitions and reservation lifecycle."""
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Warehouse:
    available: dict[str, int]
    reserved: dict[str, dict[str, int]] = field(default_factory=dict)


def allocate_order(warehouse: Warehouse, reference: str, items: list[dict]) -> bool:
    # Нельзя создавать второй резерв с тем же идентификатором.
    if reference in warehouse.reserved:
        return False

    requested = {}

    # Сначала собираем суммарное количество каждого товара.
    for item in items:
        sku = str(item["sku"])
        qty = int(item["quantity"])

        if qty < 1:
            raise ValueError("Quantity must be positive")

        requested[sku] = requested.get(sku, 0) + qty

    # Проверяем все товары до изменения складских остатков.
    for sku, quantity in requested.items():
        if warehouse.available.get(sku, 0) < quantity:
            return False

    # Изменяем склад только после успешной проверки.
    for sku, quantity in requested.items():
        warehouse.available[sku] -= quantity

    warehouse.reserved[reference] = requested
    return True


def release_order(warehouse: Warehouse, reference: str) -> None:
    reservation = warehouse.reserved.pop(reference, {})
    for sku, count in reservation.items():
        warehouse.available[sku] = warehouse.available.get(sku, 0) + count

def transfer_stock(source: Warehouse, target: Warehouse, sku: str, quantity: int) -> None:
    if quantity < 1 or source.available.get(sku, 0) < quantity:
        raise ValueError('Not enough stock')
    source.available[sku] -= quantity
    target.available[sku] = target.available.get(sku, 0) + quantity

def reservation_expired(created_at: str, now: datetime, minutes: int = 30) -> bool:
    created = datetime.fromisoformat(created_at)
    return (now - created).total_seconds() > minutes * 60

def stock_value(warehouse: Warehouse, prices: dict[str, int]) -> int:
    return sum(quantity * prices.get(sku, 0) for sku, quantity in warehouse.available.items())
