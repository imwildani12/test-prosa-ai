from .serializers import QuestionSerializer
from rest_framework import generics
from rest_framework.response import Response


class QuestionView(generics.CreateAPIView):
    authentication_classes = []
    serializer_class = QuestionSerializer

    def post(self, request):
        question_serializer = QuestionSerializer(data=request.data)
        
        if question_serializer.is_valid():
            question = question_serializer.save()
            resp = {
                "msg": question.answer
            }
            
            return Response(resp, status=200)
        
        return Response(question_serializer.errors, status=400)