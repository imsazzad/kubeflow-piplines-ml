from kfp import dsl


def deploy_model_op(model):
    return dsl.ContainerOp(
        name='Deploy Model',
        image='sazzadbuet08/kubeflow-pipelines-ml:deploy',
        arguments=[
            '--model', model
        ]
    )