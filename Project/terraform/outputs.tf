output "pubsub_topic" {
  value = google_pubsub_topic.topic.name
}

output "artifact_registry" {
  value = google_artifact_registry_repository.repo.name
}

output "bq_dataset" {
  value = google_bigquery_dataset.dataset.dataset_id
}
