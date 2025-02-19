terraform {
  required_version = ">= 1.0"
  backend "s3" {
    bucket  = "mlfow-aws-bucket-remote"
    key     = "mlops-zoomcamp-stg.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current_identity" {}

locals {
  account_id = data.aws_caller_identity.current_identity.account_id
}

# ride_events
module "source_kinesis_stream" {
  source           = "./modules/kinesis"
  retention_period = 48
  shard_count      = 2
  stream_name      = "${var.source_stream_name}-${var.project_id}"
  tags             = var.project_id
}

# ride_predictions
module "output_kinesis_stream" {
  source           = "./modules/kinesis"
  retention_period = 48
  shard_count      = 2
  stream_name      = "${var.output_stream_name}-${var.project_id}"
  tags             = var.project_id
}

# model bucket
module "s3_bucket" {
  source      = "./modules/s3"
  bucket_name = "${var.model_bucket}-${var.project_id}"
}

