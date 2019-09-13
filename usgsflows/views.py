from django.shortcuts import render
from .models import Flow
from django.views.generic.list import ListView
from rest_framework import viewsets
from .serializers import FlowSerializer


class FlowListView(ListView):
    model = Flow


class FlowViewSet(viewsets.ModelViewSet):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer
