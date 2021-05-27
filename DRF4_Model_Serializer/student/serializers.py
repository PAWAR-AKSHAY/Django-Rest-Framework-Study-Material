from rest_framework import serializers
from student import models


class StudentSerializer(serializers.ModelSerializer):

    # Validators
    def start_with_l(value):
        if value[0].lower() != 'l':
            raise serializers.ValidationError('Name should be start with L')

    name = serializers.CharField(validators=[start_with_l])

    # For single value
    # name = serializers.CharField(read_only=True)  # Write operation will not be performed on name field

    class Meta:
        model = models.Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']  # For multiple values
        # extra_kwargs = {
        #     'name': {'read_only': True},
        #     'roll': {'read_only': True},
        # }

    def validate_roll(self, value):
        """ Field level validation """
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):
        """ Object level validation """
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'waller ' and ct.lower() != 'pune':
            raise serializers.ValidationError('City must be pune')
        return data

