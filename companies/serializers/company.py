from rest_framework import serializers
from companies.models import CompanyGroup


class CompanyGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyGroup
        fields = ('id', 'name', 'slug', 'active', 'user', 'created', 'updated')
        extra_kwargs = {'slug': {'read_only': True, 'required': False}}
