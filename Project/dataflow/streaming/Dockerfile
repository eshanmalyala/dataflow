# Use Google’s official Flex Template base image
FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

WORKDIR /dataflow/template

COPY streaming/streaming_pipeline.py .
COPY common/masking_utils.py common/masking_utils.py

RUN pip install --upgrade pip && \
    pip install google-cloud-pubsub google-cloud-bigquery

ENTRYPOINT ["/opt/google/dataflow/python_template_launcher", "--launcher_binary", "--flex-template-python-module", "streaming_pipeline"]
