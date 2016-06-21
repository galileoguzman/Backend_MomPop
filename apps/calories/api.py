from tastypie.resources import ModelResource
from .models import Calorie


class CaloriResource(ModelResource):
    class Meta:
        queryset = Calorie.objects.all()
        resource_name = 'calories'