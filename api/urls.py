from django.urls import path
from .views import NormasList, NormasDetail

app_name = 'normas_api'

urlpatterns = [
    path('<int:pk>/', NormasDetail.as_view(), name='detailcreate'),
    path('', NormasList.as_view(), name='listcreate'),
]