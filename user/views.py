from rest_framework.viewsets import ModelViewSet
from .serializers import SessionSerializer
from .models import Session

# Create your views here.
class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer