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