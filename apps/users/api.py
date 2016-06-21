from tastypie.resources import ModelResource
from .models import User, Food


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'




class FoodResource(ModelResource):
    class Meta:
        queryset = Food.objects.all()
        resource_name = 'foods'