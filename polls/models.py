from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    probability = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
@python_2_unicode_compatible  # only if you need to support Python 2
class Client(models.Model):
    #id_clt = models.CharField(max_length=200)
    nom_clt = models.CharField(max_length=200)
    prenom_clt = models.CharField(max_length=200)
    adrs_clt = models.CharField(max_length=200)
    num_tel_clt = models.CharField(max_length=200)
    email_clt = models.CharField(max_length=200)
    login_clt = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_clt
