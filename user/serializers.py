from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    hashtag = serializers.SerializerMethodField()

    class Meta:
        model = Session
        fields = ['sessionID', 'userID', 'date', 'quiz', 'summary', 'hashtag']

    def get_hashtag(self, obj):
        return list(obj.hashtag.values_list('hashtag', flat=True))
