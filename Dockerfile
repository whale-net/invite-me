FROM python:3.11-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /opt

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev


# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
# TODO - may not actually need to copy over bin
ADD ./bin ./bin
ADD ./invite_me ./invite_me
ADD ./pyproject.toml .
ADD ./uv.lock .
ADD ./README.md .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

#RUN uv pip install .
RUN uv sync

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

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


CMD ["uv", "run", "opentelemetry-instrument", "python", "bin/hello_world_forever.py"]
