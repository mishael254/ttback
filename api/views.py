from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer,FeedbackSerializer
from rest_framework import generics
from .models import Feedback

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

@api_view(['POST'])
def create_member(request):
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_member(request):

    if request.method == 'POST':
        member = Member.objects.all()

        return render(request, 'members.html', {'member': member})