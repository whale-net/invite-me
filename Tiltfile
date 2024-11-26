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
    set=[
        'inviteme.image.repository=invite-me',
        'inviteme.otelCollector.logs.endpoint=invite-me.invite-me-dev.svc.cluster.localyou ',
        'otelCollector.enabled=true',
        ]
)

k8s_yaml(yaml)