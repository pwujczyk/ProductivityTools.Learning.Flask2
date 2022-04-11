from flask import request
from flask_restful import Resource
from http import HTTPStatus
from Models.recipe import Recipe, recipe_list

class RecipeListResource(Resource):
    def get(self):
        data=[]
        for recipe in recipe_list:
            if recipe.is_published is True:
                data.append(recipe.data)
        return {'data':data}, HTTPStatus.OK

    def post(self):
        data=request.get_json()
        recipe=Recipe(name=data['name'], description=data['description'], num_of_servings=data['num_of_servings'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED