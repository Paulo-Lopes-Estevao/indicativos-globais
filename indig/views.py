from django.shortcuts import render
from rest_framework import viewsets
from indig.models import Indicativos
from indig.serializers import IndicativoSerializer


# Create your views here.
class IndicativosViewSet(viewsets.ModelViewSet):
    queryset = Indicativos.objects.all()
    serializer_class = IndicativoSerializer


def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')
