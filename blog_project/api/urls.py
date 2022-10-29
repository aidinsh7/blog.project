from django.urls import include, path
from rest_framework import routers

app_name="api"
router = routers.SimpleRouter()
router.register('articles', ArticleViewset, basename='articles'),
router.register('users', UserViewSet, basename='users'),





urlpatterns = [
	path("", include(router.urls)),
]
