from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        # Add more languages as needed
    ]
    
    question = models.TextField()  # Question text
    answer = CKEditor5Field('Answer', config_name='extends')  # Answer text, can store rich text
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)  # Language of the FAQ

    def __str__(self):
        return f"FAQ: {self.question} ({self.language})"
    
    class Meta:
        unique_together = ('question', 'language')  # Ensure each FAQ-question and language pair is unique
    
    def get_translated_faq(self, lang='en'):
        """
        Fetch translated FAQ based on the requested language.
        Fallback to the default language if translation is not available.
        """
        # translation = FAQ.objects.filter(question=self.question, language=lang).first()
        # if translation:
        #     return {
        #         'question': translation.question,
        #         'answer': translation.answer,
        #     }
        # # Fallback to default language (usually English)
        # return {
        #     'question': self.question,
        #     'answer': self.answer,
        # }
