#!/usr/bin/env bash

python3 \
    /app/.venv/bin/gunicorn \
    --bind 0.0.0.0:8080 \
    --worker-tmp-dir /dev/shm \
    -k uvicorn.workers.UvicornWorker \
    app:app
