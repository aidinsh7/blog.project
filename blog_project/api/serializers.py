from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from blog.models import Article


class ArticleSerializers(DynamicFieldsMixin,serializers.ModelSerialize):
    def get_author(self, obj):
        return {
            "username":obj.author.username,
            "firstname":obj.author.firstname,
            "lastname":obj.author.lastname,
        }
        author=serializers.SerializerMethodField("get_author")
    
    
    class Meta:
        model = Article
        fields= "__all__"







class UserSerializers(serializers.ModelSerialize):
    class Meta:
        model = get_user_model()
        fields= "__all__"