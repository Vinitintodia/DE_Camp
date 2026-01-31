variable "project" {
  description = "project"
  default = "terraform-486020"
  
}

variable "region" {
  description = "GCP Region"
  default     = "us"
  
}

variable "location" {
  description = "GCP Bucket Location"
  default     = "us"

}


variable "bq_dataset" {
  description = "My BigQuery Dataset Name"
  default     = "terraform1_dataset"

}

variable "gcs_storage_bucket" {
  description = "My Storage Bucket Name"
  default     = "terraform_demo-bucket"

}

variable "gcp_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

