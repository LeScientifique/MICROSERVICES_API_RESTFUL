#!/bin/sh

echo "Waiting for mysql..."

while ! nc -z order-db 3306; do
  sleep 0.1
done

echo "mysql started"

python main.py run -h 0.0.0.0