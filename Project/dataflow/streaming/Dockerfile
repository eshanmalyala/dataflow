# Use Google Cloud Dataflow Python base image
FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

# Define Beam template configuration environment variables
ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/requirements.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/streaming_pipeline.py"

# Create working directory
WORKDIR /template

# Copy pipeline code and requirements
COPY dataflow/streaming/streaming_pipeline.py /template/
COPY dataflow/common/masking_utils.py /template/common/
COPY requirements.txt /template/

# Install required system packages and Python dependencies
RUN apt-get update && \
    apt-get install -y libffi-dev git && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ${FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE} && \
    pip download --no-cache-dir --dest /tmp/dataflow-requirements-cache -r ${FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE}

# Optional performance tweak for older Beam versions
ENV PIP_NO_DEPS=True

# Entrypoint for Dataflow Python template launcher
ENTRYPOINT ["/opt/google/dataflow/python_template_launcher"]
