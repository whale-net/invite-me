FROM python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY ./pyproject.toml /app/pyproject.toml

WORKDIR /app
RUN uv pip install --system -r pyproject.toml

COPY . /app

# need to install 'invite_me' here so celery can call to invite_me functions
RUN uv pip install --system .

WORKDIR /app/invite_me

CMD ["celery","-A", "tasks", "worker", "--autoscale", "10", "--loglevel=info"]