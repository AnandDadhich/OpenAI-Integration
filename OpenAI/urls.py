from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("chat", ChatViewSet, basename="Chat")
router.register("q&A", QuestionAnswerViewSet, basename="Q&A")
router.register("google/ads", GoogleAdsViewSet, basename="GoogleAds")

urlpatterns = [
    path('', include(router.urls))
]
