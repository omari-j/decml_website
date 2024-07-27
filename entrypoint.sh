# Fetch secrets from AWS Secrets Manager
SECRET_JSON=$(aws secretsmanager get-secret-value --secret-id decml-website-secrets --region eu-west-2 --query SecretString --output text)

# Debugging: Print fetched secrets
echo "Fetched secrets: $SECRET_JSON"

# Write secrets to .env file
{
	echo "SECRET_KEY=$(echo $SECRET_JSON | jq -r '.SECRET_KEY')"
	echo "EMAIL_HOST_USER=$(echo $SECRET_JSON | jq -r '.EMAIL_HOST_USER')"
	echo "EMAIL_HOST_PASSWORD=$(echo $SECRET_JSON | jq -r '.EMAIL_HOST_PASSWORD')"
	echo "AWS_ACCESS_KEY_ID=$(echo $SECRET_JSON | jq -r '.AWS_ACCESS_KEY_ID')"
	echo "AWS_SECRET_ACCESS_KEY=$(echo $SECRET_JSON | jq -r '.AWS_SECRET_ACCESS_KEY')"
	echo "AWS_SES_REGION_NAME=$(echo $SECRET_JSON | jq -r '.AWS_SES_REGION_NAME')"
	echo "AWS_SES_REGION_ENDPOINT=$(echo $SECRET_JSON | jq -r '.AWS_SES_REGION_ENDPOINT')"
	echo "AWS_STORAGE_BUCKET_NAME=$(echo $SECRET_JSON | jq -r '.AWS_STORAGE_BUCKET_NAME')"
	echo "DATABASE_NAME=$(echo $SECRET_JSON | jq -r '.DATABASE_NAME')"
	echo "DATABASE_USER=$(echo $SECRET_JSON | jq -r '.DATABASE_USER')"
	echo "DATABASE_PASSWORD=$(echo $SECRET_JSON | jq -r '.DATABASE_PASSWORD')"
} > /app/.env

# Debugging: Print .env file content
cat /app/.env

# Export environment variables
export $(cat /app/.env | xargs)

# Start the application using Django's development server
python decml/manage.py runserver 0.0.0.0:8000

