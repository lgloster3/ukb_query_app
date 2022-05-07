import json
import io
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator
from rest_framework.decorators import parser_classes
from rest_framework.reverse import reverse
from turtle import left
from matplotlib.pyplot import cla
import numpy as np
import pandas as pd
from dataclasses import field
# from django_pandas.io import read_frame
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection #check performance of queries

from .forms import FieldForm
from . models import DataDictionaryShowcase, Field, Encoding, Esimpint, UqueryTestdb, Ukb37912, UqueryUkb37912Test2
from . filters import FieldFilter
from django.db.models import Q 

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import *
from rest_framework.renderers import JSONRenderer


# Create your views here.

def home(request):
    return render(request,'uquery/home.html',{})

def query_builder(request):
    fields = Field.objects.only('field_num','title','instance_id','encoding')
    myfilter = FieldFilter(request.GET,queryset=fields)
    fields = myfilter.qs
    
    context = {"fields":fields, "myfilter":myfilter}
    return render(request,'uquery/query_builder.html',context)

# -------------------------------------------------------------------------Testing
#testing
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/field_list/',
        'Test':'/test_db/'
    }
    return Response(api_urls)

@api_view(['GET'])
def FieldList(request):
    fields = Field.objects.filter(field_id=87)
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def TestDb_view(request):
    #query and serialize
    db = UqueryTestdb.objects.all().order_by("id")
    serializer = TestDbSerializer(db, many=True)
    dict_data = json.loads(json.dumps(serializer.data))

    #dataframe to html
    df = pd.DataFrame(dict_data)
    categoryCols = list(df.columns)
    extends = ["{% extends 'uquery/base.html' %}","{% block content %}","{% endblock %}"]
    
    # for column in categoryCols:
    #     dummies = pd.get_dummies(df[column],prefix=column)
    #     df = pd.concat([df,dummies],axis=1)
    #     df = df.drop(columns=column)
    

    df = df.to_html(index=False, classes=['table','table-bordered','table-striped','table-hover'],justify="left")
    # extends.insert(2,df.to_html(classes=['table','table-bordered','table-striped','table-hover']))
    # with open ("C:\\Users\\Logan\\Desktop\\ukb_query_app\\ukb_query_app\\ukb_query_app\\uquery\\templates\\uquery\\table.html","w") as file:
    #     for i in range(len(extends)):
    #         file.writelines(extends[i]+ "\n")
    #         print(extends[i])
            
    
    return render(request,'uquery/table.html',{})

# @api_view(['GET'])
# def OneHotEncode(request):
#     #query patient db
#     fid = '3809'
#     assess = '0'
#     index = '0'
#     # db = Ukb37912.objects.filter(data__field=field_id).filter(data__assessment=assess).filter(data__index=index).order_by('data__value')
#     # db = UqueryUkb37912Test2.objects.filter(data__field=fid).filter(data__assessment=assess).filter(data__index=index).order_by('data__value')
#     db = UqueryUkb37912Test2.objects.filter(
#         Q(data__field__in=['87','3809']) & 
#         Q(data__assessment=assess) & 
#         Q(data__index=index)
#         )
#     # db2 = UqueryUkb37912Test2.objects.filter(data__field__in=['87','3809'])
#     #serialize json convert patient data
#     serializerU = UKBSerialTest2(db, many=True)
#     dict_data = json.loads(json.dumps(serializerU.data))

#     #query for field_id vals
#     es_vals = Esimpint.objects.filter(fk_encoding_esimpint__in=Encoding.objects.filter(field__field_fk__in=['87','3809']).values_list("encoding_id",flat=True))
#     serializerE = EsimpintSerializer(es_vals,many=True)
#     dict_data2 = JSONRenderer().render(serializerE.data)
#     stream = io.BytesIO(dict_data2)
#     esimpint_clean = JSONParser().parse(stream)

#     #normalize json into pd Dataframe
#     df = pd.json_normalize(dict_data)
#     df = df.rename(columns={"data.f.eid":"f.eid","data.index":"Index", "data.field":"Field","data.value":"Value","data.assessment":"Assessment", "data.version":"Version"})
#     df = df.drop(columns=['id',"Index","Assessment","Field", "Version"])
#     categoryCols = list(df.columns)


#     #replacing data encoding int 'value' with str 'meaning'
#     for val in df['Value']:
#         for code in esimpint_clean:
#             if int(code['value']) == int(val):
#                 df = df.replace({'Value':{val:code['meaning']}})
            
#     # one-hot encoding using pandas method
#     for column in categoryCols:
#         if column == 'Value':
#             dummies = pd.get_dummies(df[column],prefix="df"+fid)
#             df = pd.concat([df,dummies],axis=1)
#             df = df.drop(columns=column)
    
#     #converting table to html
#     df = df.to_html(index=False, classes=['table','table-bordered','table-striped','table-hover'],justify="left")

#     context = {"df":df}
    # return render(request,'uquery/ukb_test.html',context)

@api_view(['GET','POST'])
@parser_classes([JSONParser])
def OHE_Test2(request):

    if request.method == 'GET':
        fid = ['3809','87','20002']
        assess = ['0','1','2']
        index = '0'
        v = ['Integer','Date','Continuous']

       
        findDataType = Field.objects.filter(
            Q(field_num__in=fid),
            Q(instance_id__in=assess),
        )
        serialize = FieldSerializer(findDataType,many=True)
        dict_data2 = JSONRenderer().render(serialize.data)
        stream = io.BytesIO(dict_data2)
        clean = JSONParser().parse(stream)
        
        context = {"df":clean}
        
        return render(request,'uquery/ukb_test.html',context)

    if request.method == 'POST':
        serializer = TestSerializer(data = request.data, many=True)
        if serializer.is_valid():
            dict_data = JSONRenderer().render(serializer.data)
            stream = io.BytesIO(dict_data)
            clean = JSONParser().parse(stream)
            for i in clean:
                print(i['field_num'], i['title'],i['value_type'])
            return Response(clean, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(dict_data2)

    #TESTING

     # db2 = Field.objects.select_related('encoding').filter(encoding_id=3) | Field.objects.select_related('encoding').filter(encoding_id=4)
#     # db2 = Encoding.objects.select_related("esimpint").filter(esimpint__value=-3).filter(field__field_id=87)
#     # db2 = Field.objects.filter(encoding__encoding_id=3)
#     db2 = Esimpint.objects.filter(encoding__encoding_id=37)
    # db = Ukb37912.objects.filter(data__field='87').filter(data__assessment='1')
    # s = UKBSerializer(db,many=True)
    # d = json.loads(json.dumps(s.data))
    # db = Encoding.objects.filter(field__field_id=87)
    # dbserializer = EncodingSerializer(db, many=True)
    # dict_data = json.loads(json.dumps(dbserializer.data))

    # # db2 = Encoding.objects.filter(field__field_id=87).select_related('esimpint')
    # # db2 = Esimpint.objects.filter(encoding_id__in=Encoding.objects.filter(encoding_id=37).values_list('encoding_id',flat=True))
    # db2 = Esimpint.objects.filter(encoding_id__in=Encoding.objects.filter(field__field_id=6139).values_list("encoding_id",flat=True))

#     # dict_data2 = json.loads(json.dumps(serializerF.data))
#     dict_data2 = json.loads(json.dumps(serializerG.data))
    # serializerF = EncodingSerializer(db2,many=True)
#     serializerG = EsimpintSerializer(db2,many=True)
    # dbserializer2 = EsimpintSerializer(db2, many=True)
    # dict_data2 = json.loads(json.dumps(dbserializer2.data))
#CHECK SERIALIZER ERRORS AND VALIDATION (returned error 'encoding' is not unique in esimpint; although it is a compound primary key (w/ value) in postgresql)
# print(data)
    # for item in data:
    #     if item['value'] == -3:
    #         print(item['value'])
    # a = EsimpintSerializer(data=data[0])
    # b = EsimpintSerializer(data=data[1])
    # if a.is_valid():
    #     print(a.validated_data)
    # else:
    #     print(a.errors)
    # print(a)

#FAILED REPLACE CELL METHOD
                # df.replace(to_replace=row, value=code['meaning'], regex=True, inplace=True)
                # index_loc = df.index[df.Value==row].tolist()
                # index_loc = list(set(index_loc))
                # df.loc[df['Value'] == row] = code['meaning']
                # for item in index_loc:
                #     df.loc[df['Value'] ==]

#TRIED TO ADD CONDITIONAL FOR PREFIX NAME; BETTER SOLUTION ABOVE (aka just replace coded val with str meaning)
 # val_col = ""
    # for column in categoryCols:
    #     if column == "Value":
    #         for index_val in df[column]:
    #                 # if index_val.isdigit(): #this is a check to make sure the col value is ONLY numbers; then it can be converted into type(int)
    #                 #     index_val = int(index_val) #method on index_val didn't stay when index_val called later; not sure why int() didn't stick on local var reassignment
    #                 for item in data_clean:
    #                     if item['value'] == int(index_val):
    #                         val_col = item['meaning']

    #                     # dummies = pd.get_dummies(df[column],prefix="df"+field_id+val_col)
    #                     # df = pd.concat([df,dummies],axis=1)
    #                     # df = df.drop(columns=column)
    # # df = df.to_html(classes=['table','table-bordered','table-striped','table-hover'],justify="left")

    #write out html to templates file to display table

    """THIS IS NO LONGER NEEDED. USE TEMPLATE TAGS INSTEAD FOR CONTEXT VAR. EXAMPLE:

    {% autoesacpe off %}
    {{table_var}}
    {% endautoescape %}
    
    
    """
    # extends = ["{% extends 'uquery/base.html' %}","{% block content %}","{{db2}}","{% endblock %}"]
    # extends.insert(2,df.to_html(classes=['table','table-bordered','table-striped','table-hover'],justify="left"))
    # with open ("C:\\Users\\Logan\\Desktop\\ukb_query_app\\ukb_query_app\\ukb_query_app\\uquery\\templates\\uquery\\ukb_test.html","w") as file:
    #     for i in range(len(extends)):
    #         file.writelines(extends[i]+ "\n")

#sql used in postgresql to inner join on encoding_id as foreign key
# -- ALTER TABLE esimpint
# -- ADD CONSTRAINT esimpint_encoding_fk
# -- FOREIGN KEY (encoding_id)
# -- REFERENCES encoding(encoding_id)
# -- ON DELETE CASCADE;

# -- ALTER TABLE field
# -- ADD CONSTRAINT field_encoding_fk
# -- FOREIGN KEY (encoding_id)
# -- REFERENCES encoding(encoding_id)
# -- ON DELETE CASCADE;

# SELECT * FROM esimpint
# WHERE value = -3;

# SELECT value, meaning FROM field
# INNER JOIN esimpint on encoding_id=fk_encoding_id
# WHERE field.encoding_id=100347 and esimpint.fk_encoding_id=100347;

# SELECT value, meaning FROM esimpint
# INNER JOIN field on encoding_id=fk_encoding_id
# WHERE field.encoding_id=100347 and esimpint.fk_encoding_id=100347;

# SELECT 
# "field"."field_id", 
# "field"."title", 
# "field"."encoding_id", 
# "esimpint"."value",
# "esimpint"."meaning"
# FROM "field" INNER JOIN "esimpint" ON ("field"."encoding_id" = "esimpint"."fk_encoding_id") WHERE "field"."field_id" = 87;