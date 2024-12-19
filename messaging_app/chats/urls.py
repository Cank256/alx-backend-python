from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import UserViewSet, ConversationViewSet, MessageViewSet

# Initialize main router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router for messages under conversations
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),            # Main routes
    path('api/', include(conversation_router.urls)),  # Nested routes
]