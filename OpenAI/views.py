from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import openai
import os
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        openai.api_key = os.environ["OPENAI_API_KEY"]
        human_text = serializer.validated_data.get("human_text")
        response = openai.Completion.create(
            engine="davinci",
            prompt="The following is a conversation with an AI assistant. "
                   "The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?"
                   "\nAI: I am an AI created by OpenAI. How can I help you today?"
                   "\nHuman:"+human_text+"\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )
        return Response(response, status=status.HTTP_200_OK)


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionAnswerSerializer
    queryset = QuestionAnswer.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        openai.api_key = os.environ["OPENAI_API_KEY"]
        ques = serializer.validated_data.get("ques")
        response = openai.Completion.create(
            engine="davinci",
            prompt="I am a highly intelligent question answering bot. "
                   "If you ask me a question that is rooted in truth, I will give you the answer. "
                   "If you ask me a question that is nonsense, trickery, or has no clear answer, "
                   "I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\n"
                   "A: Human life expectancy in the United States is 78 years.\n\n"
                   "Q: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955."
                   "\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?"
                   "\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\n"
                   "Q: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\n"
                   "Q: How many squigs are in a bonk?\nA: Unknown\n\nQ: "+ques+"\nA:",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        return Response(response, status=status.HTTP_200_OK)


class GoogleAdsViewSet(viewsets.ModelViewSet):
    serializer_class = GoogleAdsSerializer
    queryset = GoogleAdsStruct.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        openai.api_key = os.environ["OPENAI_API_KEY"]
        company_name = serializer.validated_data.get("company_name")
        audience = serializer.validated_data.get("audience")
        description = serializer.validated_data.get("description")
        keywords = serializer.validated_data.get("keywords")

        response1 = openai.Completion.create(
            engine="davinci",
            prompt="This will generate urls by giving website name \n\nwebsite name:Ayn Infotech\nwebsite url:www.ayninfotech.com\n\nwebsite name:+"+company_name+"\nwebsite url:",
            temperature=1,
            max_tokens=20,
            top_p=1.0,
            frequency_penalty=0.1,
            presence_penalty=0.2,
            stop=["\n\n"]
        )

        response2 = openai.Completion.create(
            engine="davinci",
            prompt=description+"\n\nPlease make a table summarizing the "+company_name+" from above\n|"+company_name+"|\n",
            temperature=0.9,
            max_tokens=40,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n\n"]
        )

        response3 = openai.Completion.create(
            engine="davinci",
            prompt="Text: "+description+".\n\nProduct Keywords:"+keywords+"\n\nKeywords:",
            temperature=0.9,
            max_tokens=18,
            top_p=1.0,
            frequency_penalty=0.9,
            presence_penalty=0.0,
            stop=["\n\n"]
        )
        while None in response4:
            response4 = openai.Completion.create(
                engine="davinci",
                prompt=description+"\n\ntl;dr:",
                temperature=0.3,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.1,
                presence_penalty=0.0,
                stop=["\n\n"]
            )
            if response4 is not None:
                break

        return Response({"website_url": response1, "parsed_data": response2, "keywords": response3, "summary": response4}, status=status.HTTP_200_OK)