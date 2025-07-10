d ..
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution
