
import kfp
import kfp.components as comp
from kubernetes.client.models import V1EnvVar

@kfp.dsl.component
def test():
    # Defining component configuration
    hello_component = kfp.dsl.ContainerOp(
        name='hello-world',
        image='docker.io/mariembouhadda/hello-world:latest',
        command=['python', 'hello_world.py'],
        )
    return hello_component
@kfp.dsl.pipeline(
  name="hello world script",
  description="hello world script"
)
def hi():
    hello = test()
    hello.execution_options.caching_strategy.max_cache_staleness = "P0D"
kfp.compiler.Compiler().compile(hi, 'hello_world.zip')
client = kfp.Client(host='https://b5667049ffd46dc-dot-us-central1.pipelines.googleusercontent.com')
EXPERIMENT_NAME = 'hello world'
experiment = client.create_experiment(name=EXPERIMENT_NAME)
run = client.run_pipeline(experiment.id, 'hello world', 'hello_world.zip')
