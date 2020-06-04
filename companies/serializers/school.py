from companies.models import School, CompanyGroup, SchoolType, SchoolManager
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):

    masters = serializers.ListField(
        default=[],
        required=False,
        child=serializers.IntegerField())

    class Meta:
        model = School
        fields = ('id', 'name', 'slug', 'group', 'type', 'address', 'code', 'active', 'masters', 'created', 'updated')
        extra_kwargs = {
            'slug': {'read_only': True, 'required': False}
        }

    def create(self, validated_data):
        masters = validated_data.pop('masters', None)
        school = School.objects.create(**validated_data)

        return school

    def update(self, instance, validated_data):

        # SIGNAL : Pattern listesine signal ile güncelleme yapılıyor
        # SIGNAL : Role listesine signal ile güncelleme yapılıyor

        school_managers = SchoolManager.objects.values_list('manager_id', flat=True).filter(school_id=instance.id)

        add_manager = list(set(validated_data['masters']) - set(school_managers))
        del_manager = list(set(school_managers) - set(validated_data['masters']))

        instance.name = validated_data['name']
        instance.type_id = validated_data['type_id']
        instance.address = validated_data['address']
        instance.code = validated_data['code']
        instance.active = validated_data['active']
        instance.add_manager = add_manager
        instance.del_manager = del_manager

        # SIGNAL => Yeni yöneticiler eklenecek. Listede olmayanlar silinecek
        instance.save()

        return instance

