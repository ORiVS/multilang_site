from django.shortcuts import render
from .models import Article
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})



openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        chatbot_message = response.choices[0].text.strip()
        return JsonResponse({'message': chatbot_message})
    return JsonResponse({'error': 'Invalid request'}, status=400)
