# Bleeding-Ink
This is a single user or a single group (depends upon the number of super-user) blog application powered by django framework that provides the main function you'd 
expect from a blog app like creating blog, commenting, deleting a blog, etc..


## Features
- Material Design
- Emoji support
- Posting (for admins)
- Commenting
- Post deleting (for admins)
- Multiple image support for a post
- Other awesome features yet to be implemented

---
## Prerequisites
<p>Make sure to have a virtual environment installed in your PC preferrably conda environment.</p>

---
## Setup
Clone this repo to your desktop and run the following commands-
- activate [your environment name]
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python mange.py collectstatic
- python manage.py createsuperuser

---
## Usage
- Enter the command `python manage.py runserver`. 
- Open a browser to   `http://127.0.0.1:8000/admin/` to open the admin site.
- Create a few test objects and open `http://127.0.0.1:8000/` to see the new objects
