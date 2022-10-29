from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from blog.models import Article

from .Permissions import (IsAuthorOrReadOnly, IsStaffOrReadonly,
                          IsSuperUserOrStaffReadOnly)
from .serializers import ArticleSerializers, UserSerializers

# Create your views here.

class ArticleViewset(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    
    def get_permissions(self):
	    if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
	    else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
            return [permission() for permission in permission_classes]




class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all
    serializer_class = UserSerializers
    permission_classes=(IsSuperUserOrStaffReadOnly,)

	
	




