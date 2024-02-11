variable "aws_region" {
  description = "AWS region to create resources"
  default     = "us-east-1"
}

variable "project_id" {
  description = "project_id"
  default     = "mlops-zoomcamp"
}
variable "source_stream_name" {
  description = ""
  #stg_ride_events
}

variable "output_stream_name" {
  description = ""
  #stg_ride_predictions
}

variable "model_bucket" {
  description = "s3_bucket"
  #mlfow-aws-bucket-remote
}

