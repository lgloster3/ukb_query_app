from dataclasses import field
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import FieldForm
from . models import Field

# Create your views here.
def home(request):
    return render(request,'uquery/home.html',{})

def query_builder(request):
    submitted = False
    if request.method == "POST":
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/query_builder?submitted=True')
    else:
        form=FieldForm
        if 'submitted' in request.GET:
            submitted =True
    return render(request, 'uquery/query_builder.html',
    {'form':form,
    "submitted":submitted,
    })

def query_table(request):
    print(request.GET)
    query_dict = request.GET
    # # query = query_dict.get("name")  #<input type='text', name='query' />
    try:
        query = int(query_dict.get("query"))
    except:
        query = None
        
    field_obj = None
    if query is not None:
        field_obj = Field.objects.filter(field_id=query)
        print(field_obj)
    # fields = Field.objects.filter(field_id=)
    # print(fields)
    # if request.method == "GET":
    #     fieldID = request.GET["field_id"]
    # query = request.GET
    # query_req = query.get("query")
    # field_obj = Field.objects.get(field_id=query_req)
    # print(field_obj)
    return render(request,'uquery/query_table.html',{
        "field_obj": field_obj

    })
