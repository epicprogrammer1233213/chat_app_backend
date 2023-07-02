from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Connection
from .serializers import ConnectionSerializer

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user.profile)
