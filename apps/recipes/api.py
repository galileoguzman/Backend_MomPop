from tastypie.resources import ModelResource
from .models import Recipe


class RecipeResource(ModelResource):
    class Meta:
        queryset = Recipe.objects.all()
        resource_name = 'recipes'