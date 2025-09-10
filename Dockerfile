FROM python:3.13-slim-trixie AS builder
LABEL MAINTAINER="Pradeep Bashyal"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_PREFERENCE=only-managed

WORKDIR /app
# Install everything except the package
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --group deploy

# Sync so that Python version is installed
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --group deploy && uv build


# Final Docker Image
FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy the Python packages
COPY --from=builder /app/.venv /app/.venv

COPY --from=builder /app/dist/my_project_template-0.0.1-py3-none-any.whl /tmp/
RUN python3 -m pip install /tmp/my_project_template-0.0.1-py3-none-any.whl

COPY app.py /app/
COPY api.py /app/
COPY api-spec.yaml /app/
COPY run-app.sh /app/

# Put the uv built Python packages in the PATH
ENV PYTHONPATH="/app/.venv/lib/python3.13/site-packages/:"

# Sync the project into a new environment, asserting the lockfile is up to date
COPY pyproject.toml /app/
COPY uv.lock /app/
RUN /bin/uv sync --locked --group deploy

CMD [".venv/bin/gunicorn"  , "--bind", "0.0.0.0:8080", "--worker-tmp-dir", "/dev/shm", "app:app"]
