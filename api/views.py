from rest_framework import generics
from .models import Normas
from .serializers import NormasSerializer

class NormasList(generics.ListCreateAPIView):
    queryset = Normas.normasobjects.all()
    serializer_class = NormasSerializer

class NormasDetail(generics.RetrieveDestroyAPIView):
    queryset = Normas.objects.all()
    serializer_class = NormasSerializer