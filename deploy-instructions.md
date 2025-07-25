# Django App Runner Deployment Instructions

## Step 1: Push to GitHub
1. Create a new GitHub repository
2. Push all files in this directory to your repository

## Step 2: Create App Runner Service
Use the AWS CLI or Console with these settings:

### Service Configuration:
- **Service Name**: `django-apprunner-service`
- **Source Type**: Repository
- **Repository URL**: `https://github.com/YOUR_USERNAME/YOUR_REPO`
- **Branch**: `main`
- **Configuration Source**: Repository (uses apprunner.yaml)

### Auto-deployment:
- Enable automatic deployments for continuous deployment

## Step 3: Access Your Application
After deployment, App Runner will provide a URL like:
`https://xxxxxxxxxx.us-east-1.awsapprunner.com`

## Files Created:
✅ apprunner.yaml - App Runner build/run configuration
✅ startup.sh - Application startup script  
✅ requirements.txt - Python dependencies
✅ Django project files with WhiteNoise for static files
✅ Simple home view returning "Hello from Django on AWS App Runner!"

## Key Features:
- Python 3.8 runtime
- Gunicorn WSGI server with 2 workers
- WhiteNoise for static file serving
- Port 8000 configuration
- SQLite database (for demo purposes)
- Production-ready settings (DEBUG=False)