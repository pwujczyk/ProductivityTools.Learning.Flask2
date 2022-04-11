from http import HTTPStatus

class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe=next((recipe for recipe in recpiple_list if recipe.id==recipe_id),None)
        if recipe is None:
            return {'message':'recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.is_publish=True

        return {}, HTTPStatus.NO_CONTENT

    def __delete__(self, recipe_id):
        recipe=next((recipe for recipe in recipe_list if recipe.id==recipe_id),None)
        if recipe is None
            return {'message':'recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.is_publish=False

        return {}, HTTPStatus.NO_CONTENT