from flask_restful import Resource
from http import HTTPStatus
from flask import request
from Models.recipe import recipe_list, Recipe

class RecipeResource(Resource):
    def get(self, recipe_id):

        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id and recipe.is_publish==True),None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data=request.get_json()

        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id),None)
        if recipe is None:
            return {'message':'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name=data['name']
        recipe.description=data['description']
        recipe.num_of_servings=data['num_of_servings']

        return recipe.data, HTTPStatus.OK