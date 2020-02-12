from rest_framework import serializers
from payments.models import UserProfile, Record

class UserProfileSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(read_only=True)
    user = serializers.ReadOnlyField(source='user_id.username')
    class Meta:
        model = UserProfile
        fields='__all__'

class RecordSerializer(serializers.ModelSerializer):
    # sender = serializers.ReadOnlyField(source='sender_id.username')
    # recipient = serializers.ReadOnlyField(source='recipient_id.username')
    class Meta:
        model = Record
        fields='__all__'
