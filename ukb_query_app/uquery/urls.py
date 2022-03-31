from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('query_builder/ ', views.query_builder,name="query_builder"),
    path('api/', views.apiOverview, name="api_overview"),
    path('field_list/',views.FieldList,name="field_list"),
    path('test_db/',views.TestDb_view,name="test_db"),
    path('ukb_test/',views.OneHotEncode,name="ukb_test"),
    path('rct',include('frontend.urls'))
    
]