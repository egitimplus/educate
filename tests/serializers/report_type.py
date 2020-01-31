from rest_framework import serializers
from tests.models import ReportType


class ReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = ('test', 'report')
