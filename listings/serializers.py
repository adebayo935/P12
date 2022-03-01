from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django import forms
from datetime import datetime

class RegisterSerializer(ModelSerializer):

    def create(self, validated_data):
        data = validated_data
        new_user = User.objects.create(**data)
        new_user.set_password(data['password'])
        new_user.save()
        return new_user

    class Meta:
        model = User 
        fields = ["id","username", "team", "password",]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','team','password']


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id','first_name','last_name','email','mobile','phone','company_name','sales_contact']


class EventSerializer(ModelSerializer):     

    class Meta:
        model = Event
        fields = ['id','name','client','support_contact','contract','status','attendees','date_event','notes','created_time','updated_time']

    def update(self, instance, validated_data):
        today = datetime.now()
        instance.updated_time = today
        return instance
     


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id','client','amount','sales_contact','status','created_time','updated_time']

    def update(self, instance, validated_data):
        today = datetime.now()
        instance.updated_time = today
        return instance
        