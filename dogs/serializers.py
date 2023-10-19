from rest_framework import serializers
from dogs.models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name',
                  'size',
                  'friendliness',
                  'trainability',
                  'sheddingamount',
                  'exerciseneeds',
                ]

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.Foreign(source='breed.name')
    class Meta:
        model = Dog
        fields = ['name',
                  'age',
                  'breed',
                  'gender',
                  'color',
                  'favoritefood',
                  'favoritetoy',
                ]