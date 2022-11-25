import ipdb
from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import serializers
from rest_framework.views import status
from traits.models import Trait
from traits.serializers import TraitSerializer

from .exceptions import NonUptableKeyError
from .models import Animal, Gender


class AnimalSerializer(serializers.Serializer):
    
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=50)
        age = serializers.IntegerField()
        weight = serializers.FloatField()
        sex = serializers.ChoiceField(choices=Gender.choices, default=Gender.UNKNOW)
        
        age_in_human_years = serializers.SerializerMethodField()

        group = GroupSerializer()
        traits = TraitSerializer(many=True)

        def get_age_in_human_years(self, obj: Animal) -> str:
            return obj.convert_dog_age_to_human_years()

        def create(self, validated_data: dict):
            group_data = validated_data.pop("group")
            group_obj, _ = Group.objects.get_or_create(**group_data)

            traits_list = list()
            traits = validated_data.pop("traits")
            for trait in traits:
                obj_trait, _ = Trait.objects.get_or_create(**trait)
                # ipdb.set_trace()
                traits_list.append(obj_trait)

            new_animal = Animal.objects.create(**validated_data, group=group_obj)
            new_animal.traits.set(traits_list)

            return new_animal

        def update(self, instance: Animal, validated_data: dict):
            errors = {}
            valid_keys = {
                "traits": Trait,
                "group": Group,
                "sex": str
            }

            for key in validated_data.keys():
                if key in valid_keys:
                    message = {f"{key}": f"You can not update {key} property."}
                    errors.update(message)
        
            if len(errors) > 0:
                raise NonUptableKeyError(errors)

            for key, value in validated_data.items():
                setattr(instance, key, value)

            instance.save()

            return instance
