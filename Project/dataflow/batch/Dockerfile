FROM apache/beam_python3.11_sdk:latest

WORKDIR /dataflow/template

COPY batch_pipeline.py .
COPY ../common/masking_utils.py common/masking_utils.py

RUN pip install --upgrade pip && \
    pip install google-cloud-storage google-cloud-bigquery

ENTRYPOINT ["python", "batch_pipeline.py"]
