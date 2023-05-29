from rest_framework.viewsets import ModelViewSet
from user.serializers import SessionSerializer
from user.models import Session


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_user_id(self):
        return self.get_object().userID

    def get_session_id(self):
        return self.get_object().sessionID
