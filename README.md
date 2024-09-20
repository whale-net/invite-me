# invite-me

A service which allows invitations to be sent and accepted or declined across different mediums such as SMS and
messenger apps

## setup

```
uv venv
```

```
uv pip install .
```

## install new package

```
uv add <pkg>
```

## docker
```
docker compose up
```
### to rebuild 
```
docker compose up --build
```

### to run with reload 
```
docker compose up --watch
```

## uv notes

not sure how to pin versions
locally I (alex) am running uv-python 0.3.4
not sure how that maps

docker needs to authenticate to ghcr to build
despite being named classic, personal PAT classic seems to be the meta

```
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic
```

## logging

INSTRUMENTATION https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation
