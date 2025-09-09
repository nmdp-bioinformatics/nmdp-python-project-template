FROM python:3.13-slim-trixie

LABEL MAINTAINER="Pradeep Bashyal"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY app.py /app/
COPY api.py /app/
COPY api-spec.yaml /app/
COPY my_project_template /app/my_project_template

# Sync the project into a new environment, asserting the lockfile is up to date
COPY pyproject.toml /app/
COPY uv.lock /app/
RUN /bin/uv sync --locked --group deploy

CMD [".venv/bin/gunicorn"  , "--bind", "0.0.0.0:8080", "--worker-tmp-dir", "/dev/shm", "app:app"]
