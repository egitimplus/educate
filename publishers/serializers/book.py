from rest_framework import serializers
from publishers.models import Book, Publisher
from publishers.serializers import PublisherSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'slug', 'active', 'created', 'updated')
        extra_kwargs = {
            'slug': {'required': False},
            'active': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('question'):
            self.fields['publisher'] = PublisherSerializer(many=False)
        else:
            self.fields['publisher_id'] = serializers.IntegerField(required=False)

    def validate_publisher_id(self, value):
        publisher = Publisher.objects.filter(id=value).exists()

        if not publisher:
            raise serializers.ValidationError('Seçilen yayınevi bulunamadı.')

        return value
