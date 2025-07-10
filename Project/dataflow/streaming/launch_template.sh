#!/bin/bash
gcloud dataflow flex-template build gs://getwellsoon-bucket/templates/streaming_template.json \
  --image gcr.io/gcp-agent-garden/dataflow-streaming-pii \
  --sdk-language "PYTHON" \
  --flex-template-base-image "PYTHON" \
  --metadata-file metadata.json \
  --python-module streaming_pipeline \
  --temp-location gs://getwellsoon-bucket/tmp
