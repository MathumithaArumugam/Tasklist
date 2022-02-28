from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns=[
    path('api',views.apihandler,name='api'),
    path('api/<str:operation>/<int:dataid>',views.apihandler,name='paramsapi'),
    path('api/<str:operation>',views.apihandler,name='paramapi'),
    path('', TemplateView.as_view(template_name="bootstrap.html")),
   


   
   

]