from kfp import dsl


def preprocess_op():
    # import kfp
    # return kfp.components.func_to_container_op(name="Preprocess Data",
    #     image="sazzadbuet08/kubeflow-pipelines-ml:data-prep",
    #     arguments=["file_outputs",{
    #         'x_train': '/app/x_train.npy',
    #         'x_test': '/app/x_test.npy',
    #         'y_train': '/app/y_train.npy',
    #         'y_test': '/app/y_test.npy',
    #     }])
    return dsl.ContainerOp(
        name="Preprocess Data",
        image="sazzadbuet08/kubeflow-pipelines-ml:data-prep",
        arguments=[],
        file_outputs={
            'x_train': '/app/x_train.npy',
            'x_test': '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy',
        }
    )