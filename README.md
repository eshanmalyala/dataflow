### issue 1: 
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution

 ### fix  the issue:  
  "$$"  In cloud build args , variables like $BUCKET are missinterprted unless escaped 
   $$BUCKET tells cloud build this is a bash variable , don't try to substitute it

### issue 

Step #0: ╷
Step #0: │ Error: Error creating Topic: googleapi: Error 409: Resource already exists in the project (resource=getwellsoon-topic).
Step #0: │ 
Step #0: │   with google_pubsub_topic.topic,
Step #0: │   on main.tf line 6, in resource "google_pubsub_topic" "topic":
Step #0: │    6: resource "google_pubsub_topic" "topic" {
Step #0: │ 
Step #0: ╵
Step #0: ╷
Step #0: │ Error: googleapi: Error 412: Request violates constraint 'constraints/storage.uniformBucketLevelAccess', conditionNotMet
Step #0: │ 
Step #0: │   with google_storage_bucket.dataflow_template,
Step #0: │   on main.tf line 15, in resource "google_storage_bucket" "dataflow_template":
Step #0: │   15: resource "google_storage_bucket" "dataflow_template" {
Step #0: │ 
Step #0: ╵
Step #0: ╷
Step #0: │ Error: Error creating Dataset: googleapi: Error 409: Already Exists: Dataset gcp-agent-garden:getwellsoon_dataset, duplicate
Step #0: │ 
Step #0: │   with google_bigquery_dataset.dataset,
Step #0: │   on main.tf line 20, in resource "google_bigquery_dataset" "dataset":
Step #0: │   20: resource "google_bigquery_dataset" "dataset" {
Step #0: │ 
Step #0: ╵
Finished Step #0
ERROR
ERROR: build step 0 "hashicorp/terraform:1.6.6" failed: step exited with non-zero status: 1
