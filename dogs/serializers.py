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
    # breed = serializers.CharField(source='breed.name', read_only=True)
    breed = BreedSerializer()
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
    def create(self, validated_data):
        breed_data = validated_data.pop('breed')
        breed_instance, created = Breed.objects.get_or_create(**breed_data)
        dog_instance = Dog.objects.create(breed=breed_instance, **validated_data)
        return dog_instance