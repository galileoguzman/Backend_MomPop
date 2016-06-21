api.pyfrom tastypie.resources import ModelResource
from foods.models import Food


class FoodResource(ModelResource):
    class Meta:
        queryset = Food.objects.all()
        resource_name = 'foods'