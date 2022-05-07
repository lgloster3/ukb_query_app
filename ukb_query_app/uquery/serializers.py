from wsgiref.validate import validator
from rest_framework import serializers
from . models import *


class DataDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDictionaryShowcase
        fields = '__all__'

class EncodingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encoding
        fields = '__all__'

class EsimpintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esimpint
        fields = ['fk_encoding_esimpint','value','meaning']
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['field_num','title','instance_id','encoding', 'value_type']

class TestDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UqueryTestdb
        fields = '__all__'

class UKBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ukb37912
        fields = '__all__'

class UKBSerialTest2(serializers.ModelSerializer):
    class Meta:
        model = UqueryUkb37912Test2
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    field_num = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    instance_id = serializers.IntegerField()
    encoding = serializers.IntegerField()
    value_type = serializers.CharField(max_length=1000)

    class Meta:
        model = Field
        fields=['field_num','title','instance_id','encoding','value_type']
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=Field.objects.all(),
        #         fields=['field_num','title','instance_id','encoding','value_type'],

        #     )
        # ]