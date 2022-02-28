from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns=[
    path('Login',TemplateView.as_view(template_name="Auth.html")),
    path('api',views.apihandler,name='api'),
    path('api/<str:operation>/<int:dataid>',views.apihandler,name='paramsapi'),
    path('api/<str:operation>',views.apihandler,name='paramapi'),
    path('authapi/<str:operation>',views.authhandler,name='authapi'),
    path('tasks', TemplateView.as_view(template_name="bootstrap.html")),
    path('', views.defaultpage,name="default"),
]
