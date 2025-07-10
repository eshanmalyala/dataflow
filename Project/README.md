Before executing Cloud Build, grant the following roles to your service account `getwellsoon@gcp-agent-garden.iam.gserviceaccount.com`:

###  Required IAM Roles and GCP IAM Role Binding Commands
- roles/editor
- roles/storage.admin
- roles/bigquery.admin
- roles/pubsub.admin
- roles/artifactregistry.admin
- roles/dataflow.developer
- roles/composer.admin

- gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/editor"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/storage.admin"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/bigquery.admin"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/pubsub.admin"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.admin"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/dataflow.developer"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/composer.admin"

### Ensure all permission 
gcloud projects get-iam-policy gcp-agent-garden \
  --flatten="bindings[].members" \
  --filter="bindings.members:getwellsoon@gcp-agent-garden.iam.gserviceaccount.com" \
  --format="table(bindings.role)"


Then trigger the pipeline:
```bash
  gcloud builds submit --config=cicd/cloudbuild.yaml
```
