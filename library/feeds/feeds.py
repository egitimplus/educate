from rest_framework import serializers


class DynamicModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop("fields", None)
        exclude = kwargs.pop("exclude", None)
        depth = kwargs.pop("depth", None)
        relation = kwargs.pop('relation', None)

        if depth is not None:
                self.Meta.depth = depth

        super(DynamicModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name)



