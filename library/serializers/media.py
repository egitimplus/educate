from rest_framework import serializers
from library.models.media import Media


class MediaSerializer(serializers.ModelSerializer):

    media_file = serializers.FileField(max_length=None, use_url=True, allow_empty_file=False)

    class Meta:
        model = Media
        fields = ('id', 'media_name','media_desc','date_created','media_file')
