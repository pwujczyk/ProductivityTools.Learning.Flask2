from flask_restful import Resource
from http import HTTPStatus

class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id and recipe.is_publish=True),None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
