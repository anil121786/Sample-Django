
from django.urls import path, include
from rest_framework import routers

from .views import hello, BranchViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'branch', BranchViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/', hello),
]