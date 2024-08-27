FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY . .

RUN uv venv
RUN uv pip install .

ENV SERVICE_NAME='invite-me'


CMD ["uv", "run", "opentelemetry-instrument", "--service_name", "$SERVICE_NAME", "--logs_exporter", "console", "python", "bin/hello_world_forever.py"]
