import kfp
from kfp import dsl
from app.preprocess_data.kf_preprocess_component import preprocess_op

@dsl.pipeline(
    name='Boston Housing Pipeline',
    description='An example pipeline.'
)
def boston_pipeline():
    _preprocess_op = preprocess_op()


host='http://kf-centraldashboard.k8sdev.infolytx.tech/pipeline/'
namespace='sazzad'


client = kfp.Client(host=host, namespace=namespace)
client.create_run_from_pipeline_func(boston_pipeline, arguments={}, experiment_name= "Boston Housing Pipeline Experiment")
