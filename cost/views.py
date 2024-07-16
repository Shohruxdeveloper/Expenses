from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseView(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

