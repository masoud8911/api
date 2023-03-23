from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer
from rest_framework import status


class HomeView(APIView):
    def get(self, request):
        return Response({'name': 'masoud'})


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
