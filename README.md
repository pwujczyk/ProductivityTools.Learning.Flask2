<!--Category:react,firebase--> 
 <p align="right">
    <a href="http://productivitytools.tech/learning-flask1/"><img src="Images/Header/ProductivityTools_green_40px_2.png" /><a> 
    <a href="https://github.com/pwujczyk/ProductivityTools.Learning.ReactWithFirebaseAuthWithDb"><img src="Images/Header/Github_border_40px.png" /></a>
</p>
<p align="center">
    <a href="http://http://productivitytools.tech/">
        <img src="Images/Header/LogoTitle_green_500px.png" />
    </a>
</p>

# Learning Flask1

This repository contains my learning steps from the book **Python API Development Fundamentals - Develop a full-stack web application with Python and Flask**
<!--more-->

Install dependencies
```
pip install -r requirements.txt
```

RecipeListResource inherit after Resource, when we have **self** in the () it does not ihnerit from anything
```python
class RecipeListResource(Resource):
    def get(self):
        data=[]
        for recipe in recipe_list:
            if recipe.is_published is True:
                data.append(recipe.data)
        return {'data':data}, HTTPStatus.OK

```

## Webrequests
```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/recipes

Invoke-WebRequest -Uri http://127.0.0.1:5000/recipes -Method Post -Body (@{name='pawel'; description='dest'; num_of_servings=0} |ConvertTo-Json) -ContentType application/json
```

## Database access
Packages:
- Flask-SQLAlchemy: This is a very popular ORM package that allows us to access 
objects rather than database tables for data. With ORM, we do not need to rely on 
SQL anymore.
- Flask-Migrate: This is a package for database migration; it works on top of Alembic.
- Psycopg2-binary: This is the adapter for the Postgres database.
- Passlib: This is a password hashing library for Python.

### Create db migrations

```python 
 flask db init
 flask db migrate
 flask db upgrade
```

In the Python console in the PyCharm we can invoke expressions and operate with application

```commandline
from app import *
from models.user import User
from models.recipe import Recipe
app = create_app()
user =User(username='pawel')
with app.app_context():
    db.session.add(user)
    db.session.commit()
```