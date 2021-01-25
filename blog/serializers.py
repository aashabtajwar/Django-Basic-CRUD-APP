from rest_framework import serializers
from .models import Post # this is the model we want to serialize

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # right now we need two attributes
        # to make this work
        model = Post # the model we will serialize
        fields = '__all__' # the fields we want to display (ALL)
