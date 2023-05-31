from .models import Session, Session_hashtag
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import SessionSerializer
from .models import Session


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(userID=self.request.user)

    def create(self, request, *args, **kwargs):
        hashtag_data = request.data.pop('hashtag', [])
        data = request.data
        data['userID'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        session_instance = serializer.instance
        hashtag_objects = []

        for hashtag in hashtag_data:
            hashtag_object, _ = Session_hashtag.objects.get_or_create(
                hashtag=hashtag)
            hashtag_objects.append(hashtag_object)

        session_instance.hashtag.set(hashtag_objects)
        session_instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
