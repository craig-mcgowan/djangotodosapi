
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet)

#Wire up our API using automatic URL routing
#Include login URLS for the browsable API

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]