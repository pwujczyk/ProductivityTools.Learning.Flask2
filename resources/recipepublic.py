from http import HTTPStatus
from flask import request
from flask_restful import Resource
from Models.recipe import recipe_list

class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id),None)
        if recipe is None:
            return {'message':'recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.is_publish=True

        return {}, HTTPStatus.NO_CONTENT

    def __delete__(self, recipe_id):
        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id),None)
        if recipe is None:
            return {'message':'recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.is_publish=False

        return {}, HTTPStatus.NO_CONTENT