from kfp import dsl


def train_op(x_train, y_train):

    return dsl.ContainerOp(
        name='Train Model',
        image='sazzadbuet08/kubeflow-pipelines-ml:train',
        arguments=[
            '--x_train', x_train,
            '--y_train', y_train
        ],
        file_outputs={
            'model': '/app/model.pkl'
        }
    )
