from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, MetaData, Table, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
    Column("created_at", TIMESTAMP, default=datetime.utcnow()),
    Column("schedule_image", String, nullable=True),
    Column("hashed_password", String),
    Column("is_active", Boolean, default=True),
    Column("is_superuser", Boolean, default=False),
    Column("is_verified", Boolean, default=False),
)
