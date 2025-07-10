provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_pubsub_topic" "topic" {
  name = var.topic_id
}

resource "google_pubsub_subscription" "sub" {
  name  = "${var.topic_id}-sub"
  topic = google_pubsub_topic.topic.id
}

resource "google_storage_bucket" "dataflow_template" {
  name     = var.bucket_name
  location = var.region
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = var.dataset_id
  location                    = var.region
  delete_contents_on_destroy = true
}

resource "google_artifact_registry_repository" "repo" {
  provider      = google
  location      = var.region
  repository_id = var.artifact_registry_name
  description   = "Artifact Registry for Dataflow Flex Templates"
  format        = "DOCKER"
}
