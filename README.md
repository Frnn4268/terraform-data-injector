# AWS Terraform Data Injector 

This project creates a microservice that generates random data and stores it in an AWS RDS database. It uses AWS Lambda, API Gateway, and Terraform for infrastructure management.

### Project Structure

```plaintext
│   .gitignore
│   main.tf
│   outputs.tf
│   terraform.tfvars
│   variables.tf
│
├───.github
│   └───workflows
│           terraform-apply.yaml
│
└───scripts
        lambda_function.py
        lambda_function.zip
```

### GitHub Actions Configuration

Add the following secrets to your GitHub repository settings:

- `AWS_REGION`
- `DB_PASSWORD`
- `DB_SECRET_ARN`
- `DB_RESOURCE_ARN`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Deploying the Project

1. Initialize Terraform:

```bash
terraform init
```

2. Executes the Terraform plan:

```bash
terraform plan
```

3. Apply the Terraform configuration:

```bash
terraform apply
```

4. The `API URL` will be output upon successful deployment.

5. Destroy the Terraform configuration:

```bash
terraform destroy
```

### Usage
Make a `POST` request to the `API URL` to generate random data and store it in the RDS database.

