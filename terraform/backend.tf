# =====================================================
# SAMPLE backend.tf
# This is only a sample configuration.
# Replace bucket, key, region, and DynamoDB table
# with your own values before using it.
# =====================================================

terraform {
  backend "s3" {
    bucket         = "sample-terraform-state-bucket"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"

    # Enables state locking to prevent multiple
    # users from modifying the state simultaneously.
    dynamodb_table = "sample-terraform-locks"

    # Encrypt the state file stored in S3.
    encrypt = true
  }
}