from rest_framework import serializers
from .models import User, Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'phone_number', 'role', 'conversations']