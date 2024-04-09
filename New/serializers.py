from dataclasses import fields
from rest_framework import serializers
from .models import Publisher, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields =  '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Publisher
        fields =  '__all__'