from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GreetingViewset

router = DefaultRouter()
router.register('greet', GreetingViewset, basename='greet')

urlpatterns = [
    path('', include(router.urls)),
]
