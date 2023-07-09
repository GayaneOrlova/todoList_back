from rest_framework import serializers
from todos.models import Todo
from django_filters import rest_framework as filters


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'value', 'checked',]

class TodoFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields = ['checked']
    
