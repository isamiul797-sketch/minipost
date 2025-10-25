Features

- User Authentication
Register, Login, Logout
Password hashing (built-in Django auth)

- Posts
Create, Edit, Delete posts
Optional image upload for each post
Posts are associated with their creators

- Search
Search posts by text

- Static & Media
Proper static files handling with collectstatic
Media upload for images

- Responsive UI
Bootstrap 5 used for clean layout
Custom navbar with Home, Register, Login, Logout buttons

Tech Stack

- Python 3.13
- Django 5.2.7
- Bootstrap 5
- SQLite (default DB)
- django-widget-tweaks

Clone the Project
git clone https://github.com/isamiul797-sketch/minipost.git
cd minipost

Installation

1. Create virtual environment & activate
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

3. Apply migrations
python manage.py makemigrations
python manage.py migrate

4. Collect static files
python manage.py collectstatic --noinput

5. Run the development server
python manage.py runserver

Usage

- Register a user
Navigate to /posts/register/ and create a new account.

- Login
Navigate to /accounts/login/ to login.

- Create a post
Once logged in, go to /posts/create/ to create a new post.

- Edit/Delete post
Posts can be edited or deleted only by the author.

- Search posts
Use the search bar in the navbar to search posts by text.

Requirements
asgiref==3.10.0
Django==5.2.7
django-widget-tweaks==1.5.0
pillow==12.0.0
sqlparse==0.5.3
tzdata==2025.2

Author

Samiul Islam Sami

Django Backend Developer | Web Enthusiast
