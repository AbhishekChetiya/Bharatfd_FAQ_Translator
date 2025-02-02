from django.shortcuts import render, redirect
from .models import FAQ
from googletrans import Translator

def add_faq(request):
    if request.method == 'POST':
        # Get form data
        language = request.POST.get('language')
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        # Save the FAQ
        translator = Translator() 
        question = translator.translate(question, dest=language).text
        answer = translator.translate(answer, dest=language).text
    
        f = FAQ.objects.create(
            language=language,
            question=question,
            answer=answer
        )
        return redirect('faq_list')  # Redirect to FAQ list page

    return render(request, 'faqs_add.html')

def faq_list(request):
    lang = request.GET.get('lang', 'en')  # Default to English
    faqs = FAQ.objects.filter(language = lang)  # Fetch FAQs in default language (English)
    print(faqs)
    print(lang)
    # Translate FAQs to the selected language
    
    return render(request, 'faqs_list.html', {'faqs': faqs, 'lang': lang})