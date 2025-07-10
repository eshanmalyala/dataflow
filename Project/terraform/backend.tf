terraform {
  backend "gcs" {
    bucket  = "getwellsoon-bucket"
    prefix  = "terraform/state"
  }
}
