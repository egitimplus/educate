from rest_framework import serializers
from publishers.models import Source
from publishers.serializers import BookSerializer


class RecursiveSourceSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id', 'name', 'slug', 'sort_order', 'parent', 'book', 'active', 'created', 'updated')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('question'):
            self.fields['book'] = BookSerializer(many=False, context={'question': True})
        else:
            self.fields['source_parent'] = RecursiveSourceSerializer(many=True, read_only=True)



