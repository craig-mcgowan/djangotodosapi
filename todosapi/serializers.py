from socket import herror
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Todo
    fields = ('id','text', 'complete')
