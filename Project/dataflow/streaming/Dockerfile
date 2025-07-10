# Base image with Dataflow Python launcher
FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

# Required working directory inside container
WORKDIR /dataflow/template

# Copy files into container
COPY streaming_pipeline.py .
COPY ../common/masking_utils.py common/masking_utils.py

# Install dependencies
RUN pip install --upgrade pip && \
    pip install google-cloud-pubsub google-cloud-bigquery

# Tell Dataflow which file to run
ENV FLEX_TEMPLATE_PYTHON_PY_FILE=streaming_pipeline.py
