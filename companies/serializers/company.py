from rest_framework import serializers
from django.contrib.auth import get_user_model
from companies.models import CompanyGroup



class CompanyGroupSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)

    class Meta:
        model = CompanyGroup
        fields = ('id', 'name', 'slug', 'active', 'user_id', 'created', 'updated')
        extra_kwargs = {'slug': {'read_only': True, 'required': False}}

    def validate_user_id(self, value):
        User = get_user_model()

        # kullanıcı veritabanında kayıtlı mı kontrolü
        user = User.objects.filter(id=value).exists()

        if not user:
            raise serializers.ValidationError('Seçilen üye bulunamadı.')

        return value

    def create(self, validated_data):
        # SIGNAL : Role listesine signal ile ekleme yapılıyor
        # SIGNAL : Pattern listesine signal ile ekleme yapılıyor
        company = CompanyGroup.objects.create(**validated_data)

        return company

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.active = validated_data['active']
        instance.save()

        return instance