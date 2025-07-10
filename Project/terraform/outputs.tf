output "pubsub_topic" {
  value = google_pubsub_topic.topic.name
}

output "artifact_registry" {
  value = google_artifact_registry_repository.repo.name
}

output "bq_dataset" {
  value = google_bigquery_dataset.dataset.dataset_id
}

output "dataflow_template_bucket" {
  value = google_storage_bucket.dataflow_template.name
}

output "composer_dag_bucket" {
  value = google_composer_environment.env.config[0].dag_gcs_prefix
}
