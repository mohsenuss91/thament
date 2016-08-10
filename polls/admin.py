from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
# from .models import Client,Vendeur, Administrateur, Produit, Categorie
# from .models import Panier, Commande, Facture, Message

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

# HKA 10.08.2016 inhance the display of the model Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# admin.site.register(Client)
# admin.site.register(Vendeur)
# admin.site.register(Administrateur)
# admin.site.register(Produit)
# admin.site.register(Categorie)
# admin.site.register(Panier)
# admin.site.register(Commande)
# admin.site.register(Facture)
# admin.site.register(Message)

