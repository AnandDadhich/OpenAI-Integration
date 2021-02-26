from rest_framework import serializers
from .models import *


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"


class GoogleAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAdsStruct
        fields = "__all__"