from rest_framework import serializers
from .models import User, Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()  # Custom field for sender's name

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'conversation', 'message_body', 'sent_at']

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"


class ConversationSerializer(serializers.ModelSerializer):
    participants_names = serializers.SerializerMethodField()  # Custom field for participant names

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'participants_names', 'created_at']

    def get_participants_names(self, obj):
        return [f"{participant.first_name} {participant.last_name}" for participant in obj.participants.all()]


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()  # Custom field for full name
    role = serializers.CharField(required=True)  # Explicitly define role for validation

    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'full_name', 'phone_number', 'role', 'created_at']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def validate_email(self, value):
        """
        Validate that the email is not from a restricted domain (example.com).
        """
        restricted_domains = ['example.com']
        domain = value.split('@')[-1]
        if domain in restricted_domains:
            raise serializers.ValidationError(f"Emails from '{domain}' are not allowed.")
        return value

    def validate_role(self, value):
        """
        Validate that the role is one of the allowed values.
        """
        valid_roles = ['guest', 'host', 'admin']
        if value not in valid_roles:
            raise serializers.ValidationError(f"Role must be one of {valid_roles}.")
        return value