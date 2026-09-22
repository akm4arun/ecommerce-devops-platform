variable "aws_region" {
  description = "AWS region for the development environment"
  type        = string
  default     = "ap-south-2"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}