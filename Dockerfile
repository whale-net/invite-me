FROM python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY ./pyproject.toml /app/pyproject.toml

WORKDIR /app
RUN uv pip install --system -r pyproject.toml

COPY . /app

ENV OTEL_SERVICE_NAME='invite-me'
# ENV OTEL_TRACES_EXPORTER=console,otlp 
# ENV OTEL_METRICS_EXPORTER=console 
ENV OTEL_LOGS_EXPORTER=console,otlp
# could just use OTEL_EXPORTER_OTLP_ENDPOINT
ENV OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=0.0.0.0:4317
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_EXPORTER_OTLP_INSECURE=true

# # temp
# ENV GRPC_VERBOSITY=debug
# ENV GRPC_TRACE=http,call_error,connectivity_state

EXPOSE 8000/tcp

#CMD ["uv", "run", "opentelemetry-instrument", "python", "bin/hello_world_forever.py"]
WORKDIR /app/invite_me
CMD ["uv", "run", "fastapi", "dev", "main.py","--host", "0.0.0.0", "--port", "8000"]