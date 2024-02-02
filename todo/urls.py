from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet,todo_list

router = DefaultRouter()
router.register('api/',TodoViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('list/', todo_list)
]
