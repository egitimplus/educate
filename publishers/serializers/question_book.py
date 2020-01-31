from rest_framework import serializers
from publishers.models import Book
from .publisher import PublisherSerializer


class QuestionBookSerializer(serializers.ModelSerializer):

    publisher = PublisherSerializer(many=False)

    class Meta:
        model = Book
        fields = ('id', 'name', 'slug', 'publisher', 'active', 'created', 'updated')