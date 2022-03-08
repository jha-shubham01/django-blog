# Django Blog

# Description
This project is a simple blogging application just by using Django (and Django template) with the help of Class-Based Views.

## Features
- Login to the app
- Register on the app
- List Blog Post
- See all the Blogs without logging into the app
- Upload Hero Image on the Blog
- Create, Update, Delete Blog Post
- Archive, Draft and Publish Status for the Post
- Comment on the Blog Post
- Approve, Reject the Comment on the Blog Post before the comment is published
  

## Technology Stack
Backend: Django

## To run the project
Prerequisites: Python3, virutalenv

1. Checkout the code
2. Create a virtual environment (virutalenv .env)
3. Activate the environment (source .env/bin/activate)
4. Install all the packages (pip install -r requirements.txt)
5. Navigate inside the project (cd src)
6. Migrate (python manage.py migrate)
7. Create a superuser (python manage.py createsuperuser) <br />
   Fill in all the details on the terminal to create the super user
8. Run the backend server (python manage.py runserver)
9. Visit the server link (http://localhost:8000/)


### Future Scope
- Better UI.
- Send an Email on registration, comment.
- Forgot password feature.
- Like the Blog.
- Views count on the Blog.


### Learn from the Video Series:
https://www.youtube.com/playlist?list=PLdLYbRBk3sGnuLMIroB86PCYvWvJOTDTn
