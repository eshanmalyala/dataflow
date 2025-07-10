FROM apache/beam_python3.11_sdk:latest

WORKDIR /app

COPY dataflow/streaming/streaming_pipeline.py .
COPY dataflow/common/masking_utils.py common/masking_utils.py

RUN pip install --upgrade pip && \
    pip install google-cloud-pubsub google-cloud-bigquery

ENTRYPOINT ["python", "streaming_pipeline.py"]

# FROM apache/beam_python3.11_sdk:latest

# WORKDIR /app

# COPY dataflow/streaming/streaming_pipeline.py .
# COPY dataflow/common/masking_utils.py common/masking_utils.py

# RUN pip install --upgrade pip && \
#     pip install google-cloud-pubsub google-cloud-bigquery

# ENTRYPOINT ["python", "streaming_pipeline.py"]
