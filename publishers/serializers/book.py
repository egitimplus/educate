from rest_framework import serializers
from publishers.models import Book, Publisher


class BookSerializer(serializers.ModelSerializer):

    publisher_id = serializers.IntegerField(required=False)

    class Meta:
        model = Book
        fields = ('id', 'name', 'slug', 'publisher_id', 'active', 'created', 'updated')
        extra_kwargs = {
            'slug': {'required': False},
            'active': {'required': False},
        }

        def validate_publisher_id(self, value):
            publisher = Publisher.objects.filter(id=value).exists()

            if not publisher:
                raise serializers.ValidationError('Seçilen yayınevi bulunamadı.')

            return value
