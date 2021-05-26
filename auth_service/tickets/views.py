from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Ticket
from .serializer import TicketSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def can_access(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    user = request.user
    if ticket.user == user:
        return Response(data={'msg': 'can access'}, status=status.HTTP_200_OK)
    return Response(data={'msg': 'can\'t access'}, status=status.HTTP_403_FORBIDDEN)
