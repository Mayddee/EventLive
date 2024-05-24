from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.decorators import api_view

from .models import  Event, Booking
from users.models import User
from users.serializers import UserSerializer


# class EventSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     category = serializers.CharField()
#     description = serializers.CharField()
#     location = serializers.CharField()
#     ticket_cost= serializers.IntegerField()
#     participants = UserSerializer(many=True)
#     date = serializers.DateTimeField()
#     seats = serializers.IntegerField()
#     available_seats = serializers.IntegerField()
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()

#     def create(self, validated_data):
#         instance = Event.objects.create(name=validated_data.get("name"),
#                                             category=validated_data.get("category"),
#                                             description=validated_data.get("description"),
#                                             location=validated_data.get("location"),
#                                             ticket_cost=validated_data.get("ticket_cost"),
#                                             participants=validated_data.get("participants"),
#                                             date=validated_data.get("date"),
#                                             seats=validated_data.get('seats'),
#                                             available_seats=validated_data.get('available_seats'),
#                                             created=validated_data.get("created"),
#                                             updated=validated_data.get("updated"))
#         return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.name=validated_data.get("name")
    #     instance.description=validated_data.get("description")
    #     instance.location=validated_data.get("location")
    #     instance.ticket_cost=validated_data.get("ticket_cost")
    #     instance.participants=validated_data.get("participants")
    #     instance.date=validated_data.get("date")
    #     instance.created=validated_data.get("created")
    #     instance.updated=validated_data.get("updated")
    #     instance.save()
    #     return instance

class BookingSerializer(serializers.ModelSerializer):
    participant = UserSerializer()
    event = EventSerializer()
    class Meta:
        model = Booking
        fields = ("id", "participant", "event", "details")

