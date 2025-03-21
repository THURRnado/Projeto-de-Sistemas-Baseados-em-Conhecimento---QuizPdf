from django.urls import path
from .views import inicio, listaQuestoes, formQuestao, question_generator

urlpatterns = [
    path('', inicio ,name='inicio'),
    path('listaQuestoes/', listaQuestoes ,name='listaQuestoes'),
    path('formQuestao/', formQuestao ,name='formQuestao'),
    path('question_generator/', question_generator ,name='question_generator'),
]