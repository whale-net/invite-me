docker_build(
    'invite-me',
    context='.',
    live_update=[
        # TODO update
        sync('.', '/opt'),
        run('source .venv/bin/activate && uv pip install .', trigger='./uv.lock')
    ]
)

# create otel collector
k8s_yaml([
    'charts/invite-me/dev/otel_collector/config.yaml',
    'charts/invite-me/dev/otel_collector/deployment.yaml',
    'charts/invite-me/dev/otel_collector/service.yaml'
])

# create postgres
k8s_yaml([
    'charts/invite-me/dev/postgres/statefulset.yaml',
    'charts/invite-me/dev/postgres/service.yaml'
])

# create invite-me app
k8s_yaml(
    helm(
        'charts/invite-me',
        name='invite-me',
        namespace='invite-me-dev',  # appending '-dev' just in case this is ever ran from prod cluster
        values=['charts/invite-me/dev/dev_values.yaml'],
    )
)