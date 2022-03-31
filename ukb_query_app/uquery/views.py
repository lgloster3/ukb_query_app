import json
from turtle import left
from matplotlib.pyplot import cla
import numpy as np
import pandas as pd
from dataclasses import field
# from django_pandas.io import read_frame
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection #check performance of queries
from .forms import FieldForm
from . models import Field, TestDb, Ukb37912
from . filters import FieldFilter

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import FieldSerializer, TestDbSerializer, UKBSerializer

# Create your views here.

def home(request):
    return render(request,'uquery/home.html',{})

def query_builder(request):
    fields = Field.objects.all()
    myfilter = FieldFilter(request.GET,queryset=fields)
    fields = myfilter.qs
    
    context = {"fields":fields,"myfilter":myfilter}
    return render(request,'uquery/query_builder.html',context)

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

# -------------------------------------------------------------------------Testing

@api_view(['GET'])
def TestDb_view(request):
    #query and serialize
    db = TestDb.objects.all().order_by("id")
    serializer = TestDbSerializer(db, many=True)
    dict_data = json.loads(json.dumps(serializer.data))

    #dataframe to html
    df = pd.DataFrame(dict_data)
    categoryCols = list(df.columns)
    extends = ["{% extends 'uquery/base.html' %}","{% block content %}","{% endblock %}"]
    
    for column in categoryCols:
        dummies = pd.get_dummies(df[column],prefix=column)
        df = pd.concat([df,dummies],axis=1)
        df = df.drop(columns=column)
    
    extends.insert(2,df.to_html(classes=['table','table-bordered','table-striped','table-hover']))
    with open ("C:\\Users\\Logan\\Desktop\\ukb_query_app\\ukb_query_app\\ukb_query_app\\uquery\\templates\\uquery\\table.html","w") as file:
        for i in range(len(extends)):
            file.writelines(extends[i]+ "\n")
            print(extends[i])
            
    
    return render(request,'uquery/table.html',{})

@api_view(['GET'])
def OneHotEncode(request):
    #query and serialize
    #db = Ukb37912.objects.values('data__assessment')
    db = Ukb37912.objects.filter(data__field='87').filter(data__assessment='1').filter(data__index='1')
    serializer = UKBSerializer(db, many=True)
    dict_data = json.loads(json.dumps(serializer.data))
    

    df = pd.json_normalize(dict_data)
    df = df.rename(columns={"data.f.eid":"f.eid","data.index":"Index", "data.field":"Field","data.value":"Value","data.assessment":"Assessment"})
    categoryCols = list(df.columns)
    extends = ["{% extends 'uquery/base.html' %}","{% block content %}","{% endblock %}"]
    
    for column in categoryCols:
        dummies = pd.get_dummies(df[column],prefix=column)
        df = pd.concat([df,dummies],axis=1)
        df = df.drop(columns=column)
    
    extends.insert(2,df.to_html(classes=['table','table-bordered','table-striped','table-hover'],justify="left"))
    with open ("C:\\Users\\Logan\\Desktop\\ukb_query_app\\ukb_query_app\\ukb_query_app\\uquery\\templates\\uquery\\ukb_test.html","w") as file:
        for i in range(len(extends)):
            file.writelines(extends[i]+ "\n")
            print(extends[i])

    
    print(df)
    context = {"df":df}
    return render(request,'uquery/ukb_test.html',context)
