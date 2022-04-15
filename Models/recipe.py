from extensions import db

recipe_list=[]

# def get_last_id(cls):
#     last_id=cls.query.last()
#     r=last_id.id+1
#     return r
    # if recipe_list:
    #     last_recipe=recipe_list[-1]
    # else:
    #     return 1
    # return last_recipe.id+1

class Recipe(db.Model):
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

    def __init__(self, id, name, description, num_of_servings):


        self.id=id
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
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_recipes(cls):
        return cls.query.all()

    @classmethod
    def get_last_id(cls):
        last_id = cls.query.count()
        r = last_id + 1
        return r

