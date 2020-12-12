from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, viewsets

from .models import Branch, Student

def hello(request):
    return HttpResponse("Hey Kumar!")


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name',)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    

class StudentSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    class Meta:
        model = Student
        fields = ('name', 'status', 'email', 'gender', 'branch_id', 'branch_name', 'upd_on', 'upd_by')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
