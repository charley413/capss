from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Q
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/samsung/Downloads/dgu-project-cfa4e50d4d6b.json"


class ReviewViewSet(viewsets.ModelViewSet):
      queryset=(Review.objects.all()
                )
      serializer_class = ReviewSerializer
      #permission_classes = [AllowAny]


      def get_queryset(self):

          qs=super().get_queryset()
          qs=qs.filter(
              Q(name=self.request.user)
          )

          return qs

      def perform_create(self, serializer):
          serializer.save(name=self.request.user)
          return super().perform_create(serializer)



      def create(self, request, *args, **kwargs):
           gcs_uri = f"gs://stt_dgu/{request.data['title']}.wav"

           client = speech.SpeechClient()
           audio = speech.types.RecognitionAudio(uri=gcs_uri)
           config = speech.types.RecognitionConfig(
               encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
               sample_rate_hertz=16000,
               language_code='ko-KR')

           operation = client.long_running_recognize(config, audio)
           response = operation.result()
           result = ""
           for res in response.results:
               result += f"{res.alternatives[0].transcript}" #고침
           #request.data._mutable = True
           request.data['content'] = result

           serializer = self.get_serializer(data=request.data)
           serializer.is_valid(raise_exception=True)
           self.perform_create(serializer)

           return Response({"msg": result}, status=status.HTTP_201_CREATED)









