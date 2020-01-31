from rest_framework import serializers
from publishers.models import Source
from publishers.serializers import RecursiveSourceSerializer


class SourceSerializer(serializers.ModelSerializer):

    source_parent = RecursiveSourceSerializer(many=True, read_only=True)

    class Meta:
        model = Source
        fields = ('id', 'name', 'slug', 'sort_order', 'parent', 'book', 'active', 'created', 'updated', 'source_parent')
