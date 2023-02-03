from django.db.models import fields
from rest_framework import serializers
from app.models import Parent, Child

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parent
        fields="__all__"


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model=Child
        fields="__all__"



