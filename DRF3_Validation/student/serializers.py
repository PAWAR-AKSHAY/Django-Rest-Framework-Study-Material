from rest_framework import serializers
from student import models


# Priority
# Validators > Field Level > Object Level

# Validators

def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name should be start with A')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_a])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return models.Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, attrs):
        nm = attrs.get('name')
        ct = attrs.get('city')

        if nm.lower() == 'lucky' and ct.lower() != 'pune':
            raise serializers.ValidationError('City must be Pune')
        return attrs
