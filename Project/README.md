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
# Use a custom Dataflow service account

gcloud iam service-accounts create getwellsoon-dataflow-service \
  --display-name "Dataflow Service Account"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/dataflow.worker"
  
  gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
  
  gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataEditor"

gcloud projects add-iam-policy-binding gcp-agent-garden \
  --member="serviceAccount:getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"

gcloud iam service-accounts add-iam-policy-binding getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com \
  --member="user:rajasekhar.malyala@capgemini.com" \
  --role="roles/iam.serviceAccountUser"
 gcloud iam service-accounts add-iam-policy-binding getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com \
  --member="user:rajasekhar.malyala@capgemini.com" \
  --role="roles/iam.serviceAccounts.actAs"



    # Direct gcloud command 
    gcloud dataflow flex-template run "streaming-pii-job-$(date +%Y%m%d-%H%M%S)" \
      --project=gcp-agent-garden \
      --region=europe-west1 \
      --template-file-gcs-location=gs://getwellsoon-bucket-demo/templates/streaming_template.json \
      --parameters=input_subscription=projects/gcp-agent-garden/subscriptions/getwellsoon-topic-sub \
      --parameters=output_table=gcp-agent-garden:getwellsoon_dataset.customer_data \
      --service-account-email=getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com
      --network=projects/gcp-agent-garden/global/networks/agent-garden-custom-vpc


 gcloud dataflow flex-template run "streaming-pii-job-$(date +%Y%m%d-%H%M%S)" \
  --project=gcp-agent-garden \
  --region=europe-west1 \
  --template-file-gcs-location=gs://getwellsoon-bucket-demo/templates/streaming_template.json \
  --parameters=input_subscription=projects/gcp-agent-garden/subscriptions/getwellsoon-topic-sub \
  --parameters=output_table=gcp-agent-garden:getwellsoon_dataset.customer_data \
  --parameters=subnetwork=regions/europe-west1/subnetworks/mcd-eu-west1-subnet1 \
  --network=projects/gcp-agent-garden/global/networks/agent-garden-custom-vpc \
  --service-account-email=getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com

