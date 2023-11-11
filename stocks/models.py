from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, MetaData, Table, Boolean, Float

from users.models import user


metadata = MetaData()

trade_stock = Table(
    "trade_stock",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('user', ForeignKey(user.c.id)),
    Column("symbol", String),
    Column("description", String),
    Column("exch", String),
    Column("stock_type", String),
    Column("open_price", Float),
    Column("high_price", Float),
    Column("low_price", Float),
    Column("bid_price", Float),
    Column("ask_price", Float),
    Column("change_percentage", Float),
    Column("prevclose", Float),
    Column("week_52_high", Float),
    Column("week_52_low", Float),
    Column("trade_date", TIMESTAMP, default=datetime.utcnow()),
)

