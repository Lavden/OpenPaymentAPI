from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from payments.models import UserProfile, Record
from payments.serializers import UserProfileSerializer, RecordSerializer
from payments.permissions import IsOwnerProfileOrReadOnly, IsAssociatedRecordOrReadOnly

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly]

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes=[IsAssociatedRecordOrReadOnly]
