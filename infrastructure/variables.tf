variable "bucket_names" {
  description = "Create S3 buckets with these names"
  type        = list(string)
  default = [
    "landing-zone",
    "processing-zone",
    "delivery-zone"
  ]
}

variable "environment" {
  default = "producao"
}

variable "account" {
  default = "741358071637"
}

variable "aws_region" {
  default = "us-east-2"
}

variable "prefix" {
  default = "prefix"
}

locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Project   = "EDC Modulo 4"
    ManagedBy = "Terraform"
    UserEmail = "matheuskraisfeld@gmail.com"
  }
}