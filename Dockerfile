FROM python:3.7

#RUN git clone https://github.com/meriembouhadda/hello_world.git

COPY hello_world_launcher.py .
COPY hello_world.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
#ARG project_id='kheopsys-data-lab'
#ARG bucket='ml-pipeline-309409_bucket'
#using bash we run the deploy script we just copied in here
ENTRYPOINT ["python","hello_world_launcher.py"]
#,"--project","ml-pipeline-309409","--bucket","ml-pipeline-309409_bucket"]
