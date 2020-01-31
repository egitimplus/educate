from rest_framework import serializers
from publishers.models import Publisher, PublisherManager
from companies.models import CompanyGroup


class PublisherSerializer(serializers.ModelSerializer):

    group_id = serializers.IntegerField(required=False)
    masters = serializers.ListField(
        default=[],
        required=False,
        child=serializers.IntegerField())

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'slug', 'active', 'group_id', 'masters', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False},
            'active': {'read_only': True, 'required': False},
        }

    def validate_group_id(self, value):
        group = CompanyGroup.objects.filter(id=value).exists()

        if not group:
            raise serializers.ValidationError('Seçilen grup bulunamadı.')

        return value

    def create(self, validated_data):
        masters = validated_data.pop('masters', None)
        publisher = Publisher.objects.create(**validated_data)

        return publisher

    def update(self, instance, validated_data):

        # SIGNAL : Pattern listesine signal ile güncelleme yapılıyor
        # SIGNAL : Role listesine signal ile güncelleme yapılıyor

        publisher_managers = PublisherManager.objects.values_list('manager_id', flat=True).filter(publisher_id=instance.id)

        add_manager = list(set(validated_data['masters']) - set(publisher_managers))
        del_manager = list(set(publisher_managers) - set(validated_data['masters']))

        instance.name = validated_data['name']
        instance.add_manager = add_manager
        instance.del_manager = del_manager

        # SIGNAL => Yeni yöneticiler eklenecek. Listede olmayanlar silinecek
        instance.save()

        return instance
