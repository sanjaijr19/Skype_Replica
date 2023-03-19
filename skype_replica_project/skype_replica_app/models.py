import mongoengine


class Profile(mongoengine.Document):
    username = mongoengine.StringField(max_length=50,unique=True,required=True)
    first_name = mongoengine.StringField(max_length=20)
    last_name = mongoengine.StringField(max_length=20)
    dob = mongoengine.DateTimeField()
    email = mongoengine.EmailField(required=True,unique=True)
    phone_no = mongoengine.IntField()
    city = mongoengine.StringField()
    state = mongoengine.StringField()
    country = mongoengine.StringField()
    profile_picture = mongoengine.ImageField(collection_name='profile_pics', size_limit=20971520, thumbnail_size=(100,100,True))





