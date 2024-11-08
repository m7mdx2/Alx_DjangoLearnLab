from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Requires user to be authenticated
def unread_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    data = [{'actor': n.actor.username, 'verb': n.verb, 'target': str(n.target), 'timestamp': n.timestamp} for n in notifications]
    return Response(data)