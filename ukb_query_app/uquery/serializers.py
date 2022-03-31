from rest_framework import serializers
from . models import Field, TestDb, Ukb37912

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['field_id','title']

class TestDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDb
        fields = '__all__'

class UKBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ukb37912
        fields = '__all__'