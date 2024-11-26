# invite-me
A service which allows invitations to be sent and accepted or declined across different mediums such as SMS and messenger apps


## setup
```
uv venv
source .venv/bin/activate
uv sync
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

#### Install 
- kubectl
- docker, docker-desktop
    - enable k8s cluster in docker-desktop settings 
- tilt

Note: we are using docker-desktop cluster. Apparently not as good as using a Kind cluster, 
but also convenient and already setup with a regular docker install.
(see ctlptl for managing a kind cluster)

#### Running Tilt
Switch kubectl config to docker-desktop.
This avoids accidentally deploying to another cluster if you were using a different context already.
Maybe tilt is smart enough to have a default, but I don't want to find out :)
```bash
kubectl config use-context docker-desktop
```

Start with `tilt up`. This will automatically build a docker image and deploy to docker desktop's k8s cluster.
```bash
tilt up
```

Now your code will run and automatically sync/rebuild whenever you make a local change

Tilt will run until you tell it to stop. Even if you ctrl+c the `tilt up`, things continue running in the background.
Tilt down will stop that. Data appears to be persisted between multiple runs
```bash
tilt down
```

#### Notes
- Tilt will provision an otel collector and postgres instance for development convenience
  - In production deployment, will use pre-existing resources and this won't matter
  - but using same config method for dev/prod should simplify deployment process

TODO:
- make use of `k8s_resource` and setup dependency chain
  - currently limited benefit for the simple config we have
- secret management interfaces


