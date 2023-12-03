#!/bin/sh

echo "Starting migrate..."
alembic upgrade head

echo "Starting server..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

exec "$@"