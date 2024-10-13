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

### to run

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

## some notes

the service exists to let you send messages to your friends, and receive a simple response

web -> rabbit -> dispatcher -> device -> web again (you have phones right?)

web -> rabbit:

    client post:
        message
        to_users
        expected response type (y/n, free text, poll)

    lookup users preference
        if preferred route is valid for response type, use this
        else fallback

        if no remaining fallback, mark the message as failed to them

    write to rabbit:
        json body indicating who the message is to, and how to send it, and any fallbacks

rabbit -> dispatcher:

    client read json

    dispatcher uses corresponding service, if available, to send the message

    if fails, begin try fallbacks 
        if fallback exists create new request
        else mark failed should track "receipts" to say when a message fails for a given service 

user -> web:

    webhooks and simple url links seem best here to handle responding to things like this. 

    will imply a simple portal that confirms or provides additional information, additional information could be from 
    the originator of the request
