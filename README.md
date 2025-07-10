### issue 1: 
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution

 ### fix  the issue:  
  "$$"  In cloud build args , variables like $BUCKET are missinterprted unless escaped 
   $$BUCKET tells cloud build this is a bash variable , don't try to substitute it

### issue 2
 Acquiring state lock. This may take a few moments...
Step #0: ╷
Step #0: │ Error: Reference to undeclared resource
Step #0: │ 
Step #0: │   on outputs.tf line 14, in output "dataflow_template_bucket":
Step #0: │   14:   value = google_storage_bucket.dataflow_template.name
Step #0: │ 
Step #0: │ A managed resource "google_storage_bucket" "dataflow_template" has not been
Step #0: │ declared in the root module.
Step #0: ╵
Finished Step #0
ERROR
ERROR: build step 0 "hashicorp/terraform:1.6.6" failed: step exited with non-zero status: 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 0 "hashicorp/terraform:1.6.6" failed: step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build 6e7923fe-eb55-415d-aa0b-67ac8b3869e9 completed with status "FAILURE"
   
