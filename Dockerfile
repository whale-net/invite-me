FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY . .

RUN uv venv
RUN uv pip install .

ENV OTEL_SERVICE_NAME='invite-me'
# ENV OTEL_TRACES_EXPORTER=console,otlp 
# ENV OTEL_METRICS_EXPORTER=console 
ENV OTEL_LOGS_EXPORTER=console,otlp
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317


CMD ["uv", "run", "opentelemetry-instrument", "python", "bin/hello_world_forever.py"]
