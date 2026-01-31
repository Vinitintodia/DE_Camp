terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  # Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  credentials = file("/workspaces/DE_Camp/terraform/keys/creds.json")
  project     = var.project
  region      = var.region
}



resource "google_storage_bucket" "gcs_bucket" {
  name          = var.gcs_storage_bucket
  location      = var.location

  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}


resource "google_bigquery_dataset" "bq_dataset" {
  dataset_id                  = var.bq_dataset
  friendly_name               = "Terraform BigQuery Dataset"
  description                 = "This dataset was created using Terraform"
  location                    = var.location
  delete_contents_on_destroy  = true
}