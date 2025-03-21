from django.shortcuts import render, redirect
from .scripts.question_generator import QuestionGenerator
from dotenv import load_dotenv
import os
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html',{})


def listaQuestoes(request):
    return render(request, 'inicio/listaQuestoes.html',{})


def formQuestao(request):
    return render(request, 'inicio/formQuestao.html',{})


def question_generator(request):
        
    try:

        load_dotenv()
        api_key = os.getenv('GROQ_API_KEY')
        question_generator = QuestionGenerator(api_key)

        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            pdf_file = request.FILES['arquivo']

            if pdf_file.content_type == 'application/pdf':
                text = question_generator.extract_text_from_pdf(pdf_file)
                questions = question_generator.get_questions_from_text(text)
                question_generator.save_questions_to_file(questions, "media/json/questions.json")
                df = question_generator.json_to_dataframe("media/json/questions.json")
                print(df)

        messages.success(request, 'Questão gerada com sucesso!')
        return redirect('listaQuestoes')
    
    except Exception as e:
        messages.error(request, f'Erro ao gerar questão: {e}')
        return redirect('formQuestao')
