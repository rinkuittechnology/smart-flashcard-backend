from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Flashcard
from .serializers import FlashcardSerializer
from .subject_detector import SubjectDetector
import random

@api_view(['POST'])
def add_flashcard(request):
    serializer = FlashcardSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    question = serializer.validated_data['question']
    subject = SubjectDetector.detect_subject(question)
    
    flashcard = Flashcard.objects.create(
        student_id=serializer.validated_data['student_id'],
        question=question,
        answer=serializer.validated_data['answer'],
        subject=subject
    )
    
    return Response({
        'message': 'Flashcard added successfully',
        'subject': subject,
        'id': flashcard.id
    }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_flashcards_by_subject(request):
    student_id = request.query_params.get('student_id')
    limit = int(request.query_params.get('limit', 5))
    
    if not student_id:
        return Response(
            {'error': 'student_id parameter is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Get all flashcards for the student
    flashcards = Flashcard.objects.filter(student_id=student_id)
    
    if not flashcards.exists():
        return Response([], status=status.HTTP_200_OK)
    
    # Group by subject
    subject_groups = {}
    for fc in flashcards:
        subject_groups.setdefault(fc.subject, []).append(fc)
    
    # Select one from each subject
    mixed_flashcards = []
    for subject, cards in subject_groups.items():
        mixed_flashcards.append(random.choice(cards))
    
    # Shuffle and limit results
    random.shuffle(mixed_flashcards)
    mixed_flashcards = mixed_flashcards[:limit]
    
    serializer = FlashcardSerializer(mixed_flashcards, many=True)
    return Response(serializer.data)