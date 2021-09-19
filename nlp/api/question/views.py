from apps.question.models import Question
from rest_framework import generics
from rest_framework.response import Response

class QuestionView(generics.GenericAPIView):

    def get(self, request, question_text):
        q = Question.objects.get(text=question_text)

        resp = {
            "message" : q.answer if q else "your question is not listed on our database, im sorry"
        }

        return Response(resp, status = 200)
