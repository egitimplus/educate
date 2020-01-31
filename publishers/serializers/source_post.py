from rest_framework import serializers
from publishers.models import Source, Book


class SourcePostSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(required=False)
    parent_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Source
        fields = ('id', 'name', 'sort_order', 'parent_id', 'book_id', 'active', 'created', 'updated')
        extra_kwargs = {
            'sort_order': {'required': False},
            'active': {'required': False},
        }

        def validate_book_id(self, value):
            book = Book.objects.filter(id=value).exists()

            if not book:
                raise serializers.ValidationError('Seçilen kitap bulunamadı.')

            return value

        def validate_parent_id(self, value):
            source = Source.objects.filter(id=value).exists()

            if not source:
                raise serializers.ValidationError('Seçilen bölüm bulunamadı.')

            return value
