from extensions import db

recipe_list=[]

def get_last_id():
    if recipe_list:
        last_recipe=recipe_list[-1]
    else:
        return 1
    return last_recipe.id+1

class Recipe:

    __tablename__='recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    num_of_servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    directions = db.Column(db.String(1000))
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now(), onupdate = db.func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

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