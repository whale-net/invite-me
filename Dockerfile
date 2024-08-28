FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY . .

RUN uv venv
RUN source .venv/bin/activate
RUN uv pip install .

ENV OTEL_SERVICE_NAME='invite-me'
# ENV OTEL_TRACES_EXPORTER=console,otlp 
# ENV OTEL_METRICS_EXPORTER=console 
ENV OTEL_LOGS_EXPORTER=console,otlp
# could just use OTEL_EXPORTER_OTLP_ENDPOINT
ENV OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=0.0.0.0:4317

# temp
ENV GRPC_VERBOSITY=debug
ENV GRPC_TRACE=http,call_error,connectivity_state


CMD ["uv", "run", "opentelemetry-instrument", "python", "bin/hello_world_forever.py"]
