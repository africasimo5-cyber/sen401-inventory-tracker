# One image is shared by the three services in docker-compose.yml.
# Each service runs a different command (migrate, api, client).
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    INVENTORY_DB=/data/inventory.db

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inventory_app/ inventory_app/
COPY data/inventory.json data/inventory.json
COPY migrate.py client.py app.py ./

EXPOSE 8000
CMD ["uvicorn", "inventory_app.api:app", "--host", "0.0.0.0", "--port", "8000"]
