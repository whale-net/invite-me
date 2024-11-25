# invite-me
A service which allows invitations to be sent and accepted or declined across different mediums such as SMS and messenger apps


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
Using otel auto logging. It works, but doesn't seem to be super well documented or stable as of writing.
Python support for logging is in alpha, so that is to be expected.

todo
- more implementation ideas: https://opentelemetry.io/blog/2023/logs-collection/
- experiemental logging impl https://github.com/open-telemetry/opentelemetry-python

Ideally we don't require an otel sidecar in each pod, I don't have those kind of resources ($$$)

INSTRUMENTATION https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation

## deployment

Artifacts:
- Docker image published to github container repository (ghcr) via github actions
- Helm chart published via github pages (TODO link) via github actions

### local dev deployment
Tilt! https://tilt.dev/. Think of it like docker-compose with hot-reload.

Install:
- kubectl, docker, docker-desktop
    - enable k8s cluster in docker-desktop 
- tilt


Using docker-desktop cluster. Apparently not as good as using kind cluster, but also convenient and already setup.
(see ctlptl for managing a kind cluster)

Set kubectl config to docker-desktop to avoid accidentally deploying to production cluster if that is current-context
```bash
kubectl config use-context docker-desktop
```

