from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from ..db.decorator import primary_key
from ..utils import Price

@dataclass
@primary_key('symbol')
class SymbolInfo:
    symbol: str
    name: str
    issuer_name: str
    desc: str
    currency: str

@dataclass
@primary_key('symbol', 'date')
class EndOfDay:
    symbol: str
    date: date
    currency: str
    low: Price
    high: Price
    open: Price
    close: Price
    change: Price
    percent_change: Decimal
    traded_volume: int
    traded_value: Price

@dataclass
class ClosePrice:
    date: date
    price: Price

ClosePrices = list[ClosePrice]