# DjangoProject 🐍📰

A full-stack Django web app with user registration, login, profile management, and blog posting features. Built using Python, Django 5+, SQLite, and Bootstrap.

---

## 🔧 Features

- User registration and login system
- Profile page with image upload
- Blog creation with thumbnail image
- Blog listing with pagination
- Blog search functionality
- Django admin interface
- Media file (image) upload support

---

## 🚀 Tech Stack

- **Backend:** Django 5.x, Python 3.13
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default)
- **Image handling:** Pillow
- **Templating:** Django Templates
- **Auth:** Django’s built-in authentication

---

## 🛠 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/AriaHassanzadeh/DjangoProject.git
cd DjangoProject

# 2. Set up virtual environment
python -m venv .venv
# Activate:
# Windows CMD
.venv\Scripts\activate.bat
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate

# 3. Install dependencies
pip install django pillow

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start server
python manage.py runserver


📁 Folder Structure :

DjangoProject/
├── myproject/         # Main Django project
├── blogapp/           # Blog app
├── core/              # User auth & profiles
├── templates/         # HTML templates
├── static/            # CSS and JS
├── media/             # Uploaded images
├── manage.py
└── README.md


👤 Author

Aria Hassanzadeh
📧 ariahassanzadeh6@gmail.com