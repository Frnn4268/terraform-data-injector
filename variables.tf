variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
}

variable "db_password" {
  description = "The password for the RDS instance"
  type        = string
  sensitive   = true
}
