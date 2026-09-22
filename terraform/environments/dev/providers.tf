provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "ecommerce-devops-platform"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
