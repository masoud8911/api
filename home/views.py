from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer
from rest_framework import status
from .permissions import AllowOrReadonlyPermission


class HomeView(APIView):
    def get(self, request):
        return Response({'name': 'masoud'})


class QuestionView(APIView):
    permission_classes = [AllowOrReadonlyPermission, ]
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': 'Success Deleted'})
