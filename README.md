# Student Management System

A modern Django web application for managing student records with user authentication and a clean, intuitive UI.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Student Management**: Add, view, edit, and delete student records
- **Department Tracking**: Organize students by department
- **Responsive Design**: Beautiful UI with gradient background and responsive layout
- **Secure Access**: Protected routes that require authentication

## Tech Stack

- **Backend**: Django 5.2.15
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3
- **Hosting**: Render

## Installation

### Prerequisites
- Python 3.14+
- pip or conda

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/student_management_system.git
cd student_management_system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional for admin panel):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

### Creating an Account
1. Navigate to the "Register" page
2. Enter your username, email, and password
3. Click "Register"
4. You'll be automatically logged in and redirected to the dashboard

### Managing Students
1. From the dashboard, click "Add New Student"
2. Fill in the student details (Name, Email, Department)
3. Click "Save Student"
4. View, edit, or delete students from the dashboard

## Project Structure

```
student_management_system/
├── student_management/      # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project URL configuration
│   └── wsgi.py             # WSGI application
├── students/               # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── forms.py            # Form definitions
│   ├── urls.py             # App URL routes
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   │   └── students/
│   │       ├── base.html               # Base template
│   │       ├── home.html               # Home page
│   │       ├── login.html              # Login page
│   │       ├── register.html           # Registration page
│   │       ├── student_list.html       # Student list
│   │       ├── student_detail.html     # Student details
│   │       ├── student_form.html       # Add/Edit student
│   │       └── student_confirm_delete.html  # Delete confirmation
│   └── migrations/         # Database migrations
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
├── Procfile               # Render deployment
├── build.sh               # Build script
├── runtime.txt            # Python version
└── README.md              # This file
```

## Deployment on Render

1. Push your code to GitHub (see below)

2. Go to [Render.com](https://render.com) and sign up

3. Create a new Web Service:
   - Connect your GitHub repository
   - Select the repository
   - Branch: `main`
   - Build Command: `bash build.sh`
   - Start Command: `gunicorn student_management.wsgi --log-file -`

4. Add environment variables:
   - `SECRET_KEY`: Generate a new Django secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: your-render-domain.onrender.com

5. Create a PostgreSQL database on Render (if using production database)

6. Add `DATABASE_URL` environment variable pointing to your PostgreSQL database

7. Deploy!

## Pushing to GitHub

1. Initialize git repository:
```bash
git init
```

2. Add all files:
```bash
git add .
```

3. Create initial commit:
```bash
git commit -m "Initial commit: Student Management System"
```

4. Add remote repository (replace with your GitHub URL):
```bash
git remote add origin https://github.com/YOUR_USERNAME/student_management_system.git
```

5. Push to GitHub:
```bash
git branch -M main
git push -u origin main
```

## Environment Variables

For production deployment, set these environment variables:

- `SECRET_KEY`: Django secret key (generate with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: PostgreSQL database URL (format: `postgresql://user:password@host:port/dbname`)

## API Endpoints

### Authentication
- `GET /home/` - Homepage
- `POST /register/` - User registration
- `POST /login/` - User login
- `GET /logout/` - User logout

### Students (Requires Authentication)
- `GET /students/` - List all students
- `POST /students/new/` - Create new student
- `GET /students/<id>/` - View student details
- `POST /students/<id>/edit/` - Edit student
- `POST /students/<id>/delete/` - Delete student

## Troubleshooting

### Database Errors
If you encounter database errors after deployment, run:
```bash
python manage.py migrate
```

### Static Files Not Loading
Ensure static files are collected:
```bash
python manage.py collectstatic --no-input
```

### Secret Key Warning
Generate a new secret key and set it as an environment variable in production.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on GitHub.

---

**Created with ❤️ using Django**
