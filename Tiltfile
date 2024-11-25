docker_build(
    'invite-me',
    context='.',
)

yaml = helm(
    'charts/invite-me',
    name='invite-me',
    namespace='invite-me-dev',  # appending '-dev' just in case this is ever ran from prod cluster
    # TODO - where to store?
    values=['charts/invite-me/values.yaml'],
    set=['image.repository=invite-me', 'otelCollector.enabled=true']
)

k8s_yaml(yaml)