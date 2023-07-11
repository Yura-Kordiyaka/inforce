from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated])
    def do_vote(self, request):
        data = request.data
        employee_id = data['employee']
        employee = Employee.objects.get(id=int(employee_id))
        if Vote.objects.filter(employee=employee).exists():
            return Response({'error': "you cannot vote twice "})
        else:
            vote = VoteSerializer(data=request.data)
            vote.is_valid(raise_exception=True)
            vote.save()
            return Response({'vote': vote.data})


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
