from django.db import models

# Create your models here.


class Chat(models.Model):
    human_text = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.human_text}'


class QuestionAnswer(models.Model):
    ques = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.ques}'


class GoogleAdsStruct(models.Model):
    company_name = models.CharField(max_length=50, null=True, blank=True)
    audience = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.company_name}'
