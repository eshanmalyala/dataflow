### issue 1: 
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution

 ### fix  the issue:  
  "$$"  In cloud build args , variables like $BUCKET are missinterprted unless escaped 
   $$BUCKET tells cloud build this is a bash variable , don't try to substitute it

### issue 2


Step #1: Step 2/6 : WORKDIR /app
Step #1:  Running in 678ff740b9ae
Step #1: Removing intermediate container 678ff740b9ae
Step #1:  489fb61c870e
Step #1: Step 3/6 : COPY streaming_pipeline.py .
Step #1:  755e14d4c81b
Step #1: Step 4/6 : COPY ../common/masking_utils.py common/masking_utils.py
Step #1: COPY failed: forbidden path outside the build context: ../common/masking_utils.py ()
Finished Step #1
ERROR
ERROR: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build e61660f6-09a2-4950-9f04-8d2629e652d1 completed with status "FAILURE"
