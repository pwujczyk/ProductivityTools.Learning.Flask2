recipe_list=[]

def get_last_id():
    if recipe_list:
        last_recipe=recipe_list[-1]
    else:
        return 1
    return last_recipe.id+1

class Recipe:
    def __init__(self, name, description, num_of_servings):
        self.id=get_last_id()
        self.name=name
        self.description=description
        self.num_of_servings=num_of_servings
        self.is_published=False

    @property
    def data(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'num_of_servings':self.num_of_servings
        }