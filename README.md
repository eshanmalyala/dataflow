### issue 1: 
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution

 ### fix  the issue:  
  "$$"  In cloud build args , variables like $BUCKET are missinterprted unless escaped 
   $$BUCKET tells cloud build this is a bash variable , don't try to substitute it

### issue 2


Step #3: Pulling image: gcr.io/google.com/cloudsdktool/cloud-sdk
Step #3: Using default tag: latest
Step #3: latest: Pulling from google.com/cloudsdktool/cloud-sdk
Step #3: Digest: sha256:99c8977b5214a2c7da1cd0a77910f37bfbc7d8c3737446b886a5c058706c4c7c
Step #3: Status: Downloaded newer image for gcr.io/google.com/cloudsdktool/cloud-sdk:latest
Step #3: gcr.io/google.com/cloudsdktool/cloud-sdk:latest
Step #3: bash: line 2: terraform: command not found
Step #3: Using bucket:
Step #3: ERROR: (gcloud.dataflow.flex-template.build) argument --metadata-file: Unable to read file [dataflow/streaming/metadata.json]: [Errno 2] No such file or directory: 'dataflow/streaming/metadata.json'
Step #3: Usage: gcloud dataflow flex-template build TEMPLATE_FILE_GCS_PATH --sdk-language=SDK_LANGUAGE (--image=IMAGE | --env=[ENV,...] --flex-template-base-image=FLEX_TEMPLATE_BASE_IMAGE --image-gcr-path=IMAGE_GCR_PATH (--go-binary-path=GO_BINARY_PATH | --jar=[JAR,...] | --py-path=[PY_PATH,...]) | [--yaml-pipeline-path=YAML_PIPELINE_PATH : --yaml-image=YAML_IMAGE]) [optional flags]
Step #3:   optional flags may be  --additional-experiments | --additional-user-labels |
Step #3:                          --cloud-build-service-account | --dataflow-kms-key |
Step #3:                          --disable-public-ips | --enable-streaming-engine |
Step #3:                          --env | --flex-template-base-image | --gcs-log-dir |
Step #3:                          --go-binary-path | --help | --image |
Step #3:                          --image-gcr-path | --image-repository-cert-path |
Step #3:                          --image-repository-password-secret-id |
Step #3:                          --image-repository-username-secret-id | --jar |
Step #3:                          --max-workers | --metadata-file | --network |
Step #3:                          --num-workers | --print-only | --py-path |
Step #3:                          --service-account-email | --staging-location |
Step #3:                          --subnetwork | --temp-location |
Step #3:                          --worker-machine-type | --worker-region |
Step #3:                          --worker-zone | --yaml-image | --yaml-pipeline-path
Step #3: 
Step #3: For detailed information on this command and its flags, run:
Step #3:   gcloud dataflow flex-template build --help
Finished Step #3
ERROR
ERROR: build step 3 "gcr.io/google.com/cloudsdktool/cloud-sdk" failed: step exited with non-zero status: 2
----------------------------------------------------------------------------------------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 3 "gcr.io/google.com/cloudsdktool/cloud-sdk" failed: step exited with non-zero status: 2
ERROR: (gcloud.builds.submit) build 884650fb-134c-4f22-b184-a9de01d7eed5 completed with status "FAILURE"
