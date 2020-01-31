from rest_framework import serializers
from tests.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'report', 'types', 'created', 'updated')
