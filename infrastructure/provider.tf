provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-741358071637"
    key    = "state/igti/edc/mod4/terraform.tfstate"
    region = "us-east-2"
  }
}
