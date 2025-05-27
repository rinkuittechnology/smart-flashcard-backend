from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'student_id', 'question', 'answer', 'subject', 'created_at']
        read_only_fields = ['id', 'subject', 'created_at']