"""
!docker login -u mariembouhadda -p sS58169362
%%writefile Dockerfile
FROM tensorflow/tensorflow
COPY ./ ./
!docker build -t mariembouhadda/hello-world .
!docker push mariembouhadda/hello-world
"""
import kfp
import kfp.components as comp
@kfp.dsl.component
def hello_world():
    # Defining component configuration
    hello_component = kfp.dsl.ContainerOp(
        name='hello-world',
        image='docker.io/mariembouhadda/hello-world',
        command=['python', 'hello_world.py'],
        )
    return hello_component
@kfp.dsl.pipeline(
  name="hello world script",
  description="hello world script"
)
def hi():
    hello = hello_world()
    hello.execution_options.caching_strategy.max_cache_staleness = "P0D"
kfp.compiler.Compiler().compile(hi, 'hello_world.zip')
client = kfp.Client(host='https://b5667049ffd46dc-dot-us-central1.pipelines.googleusercontent.com')
EXPERIMENT_NAME = 'hello world'
experiment = client.create_experiment(name=EXPERIMENT_NAME)
run = client.run_pipeline(experiment.id, 'hello world', 'hello_world.zip')
