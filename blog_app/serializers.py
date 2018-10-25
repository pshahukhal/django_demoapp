from rest_framework import serializers
from blog_app.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
