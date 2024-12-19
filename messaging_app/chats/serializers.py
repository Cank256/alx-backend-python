from rest_framework import serializers
from .models import User, Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()  # Add a custom field to display sender's full name

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'conversation', 'message_body', 'sent_at']

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"


class ConversationSerializer(serializers.ModelSerializer):
    participants_names = serializers.SerializerMethodField()  # Add a custom field to display participant names

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'participants_names', 'created_at']

    def get_participants_names(self, obj):
        return [f"{participant.first_name} {participant.last_name}" for participant in obj.participants.all()]


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()  # Add a custom field to display the user's full name
    role = serializers.CharField(required=True)  # Explicitly define role as a CharField for validation

    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'full_name', 'phone_number', 'role', 'created_at']