from django.urls import path, include
from rest_framework.routers import DefaultRouter


from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostsViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]