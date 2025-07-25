# Django App Runner Deployment

This is a simple Django application configured for AWS App Runner deployment.

## Files:
- `apprunner.yaml` - App Runner configuration
- `startup.sh` - Startup script for the application
- `requirements.txt` - Python dependencies
- `manage.py` - Django management script
- `myproject/` - Django project directory

## Deployment:
1. Push this code to a GitHub repository
2. Create an App Runner service pointing to your repository
3. App Runner will automatically build and deploy your application

## Local Testing:
```bash
pip install -r requirements.txt
python manage.py runserver
```