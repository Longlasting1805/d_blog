from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogView

router = DefaultRouter()
router.register('blogposts', BlogView, basename='blogposts')

urlpatterns = [
    path('', include(router.urls)),
    # path('blogposts/', BlogView.as_view())
]
