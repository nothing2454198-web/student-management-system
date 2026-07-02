# Deployment Guide: GitHub & Render

This guide will walk you through pushing your project to GitHub and deploying it on Render.

## Step 1: Create a GitHub Repository

### Option A: Using GitHub Web Interface
1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `student-management-system`
3. Description: `A modern Django student management system with authentication`
4. Choose **Public** or **Private** (your preference)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option B: Using GitHub CLI
```bash
gh repo create student-management-system --public --source=. --remote=origin --push
```

## Step 2: Push to GitHub

After creating the repository on GitHub, connect and push your local repository:

```bash
# Navigate to your project directory
cd "c:\Users\SHASHANK S NIRWANI\student_management_system"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/student-management-system.git

# Rename branch to main (if not already)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note**: You may be prompted to authenticate. Use:
- **Personal Access Token** (recommended): Generate one at https://github.com/settings/tokens
  - Scope: `repo` (full control of private repositories)
- Or your GitHub password (if enabled)

## Step 3: Deploy on Render

### 1. Create Render Account
- Go to [https://render.com](https://render.com)
- Sign up with your GitHub account (easiest option)

### 2. Create a New Web Service
- Click "New +" → "Web Service"
- **Connect to GitHub**: Authorize and select your repository
  - Repository: `student-management-system`
  - Branch: `main`

### 3. Configure the Service
- **Name**: `student-management` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `bash build.sh`
- **Start Command**: `gunicorn student_management.wsgi --log-file -`
- **Instance Type**: Free tier (or upgrade as needed)

### 4. Set Environment Variables
Click "Advanced" and add the following environment variables:

```
SECRET_KEY = [Generate a new key - see below]
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com
```

**Generate SECRET_KEY**: Run this in your terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy PostgreSQL Database (Optional but Recommended)
Render provides a free PostgreSQL instance:

1. In Render dashboard, click "New +" → "PostgreSQL"
2. Name: `student-management-db`
3. Database: `studentdb`
4. Copy the connection string
5. Go back to your Web Service → Environment Variables
6. Add: `DATABASE_URL = [paste the connection string]`

**Note**: The free PostgreSQL instance will be deleted after 90 days of inactivity.

### 6. Deploy
- Click "Create Web Service"
- Render will automatically build and deploy your app
- Monitor the build process in the "Events" tab
- Once complete, your app will be live at `https://your-app-name.onrender.com`

## Step 4: Post-Deployment Setup

### Run Migrations
Your `build.sh` script automatically runs migrations, but you can also:
1. Go to Render dashboard → Your service
2. Click "Shell" tab
3. Run: `python manage.py migrate`

### Create Superuser (Admin Account)
```bash
# In Render Shell
python manage.py createsuperuser
# Follow the prompts
```

### Access Your App
- Main site: `https://your-app-name.onrender.com/`
- Admin panel: `https://your-app-name.onrender.com/admin/`

## Troubleshooting

### Build Fails
- Check the "Events" tab in Render for error messages
- Common issues:
  - Missing environment variables
  - Python version mismatch (should be 3.14.0)
  - Missing dependencies in requirements.txt

### App Crashes After Deploy
- Check Render logs: "Logs" tab
- Run in Shell: `python manage.py check`
- Ensure all migrations ran

### Static Files Not Loading
In Render Shell:
```bash
python manage.py collectstatic --no-input
```

### Database Errors
In Render Shell:
```bash
python manage.py migrate
```

### Can't Connect to GitHub
- Check your Personal Access Token has `repo` scope
- On GitHub: Settings → Developer settings → Personal access tokens

## Continuous Deployment

After your first deployment, every push to the `main` branch will automatically trigger a new deployment on Render. This makes it easy to update your app!

### Deploy a New Version
```bash
# Make changes to your code
# ...

# Commit changes
git add .
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Render automatically builds and deploys!
```

## Custom Domain (Optional)

To use your own domain:
1. In Render service settings
2. Scroll to "Custom Domain"
3. Add your domain
4. Follow DNS setup instructions

## Next Steps

- Add more features to your app
- Share your live app with others
- Monitor your app in Render dashboard
- Set up custom domain for production use

---

For more help:
- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com
- GitHub Help: https://docs.github.com
