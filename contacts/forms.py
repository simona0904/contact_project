
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField()


    def send_mail(self):
        message = self.cleaned_data['message']   # local variable message which contains data introduced by user
        email = self.cleaned_data['email']       # local variable email which contains email introduced by user
        email_message = f"""
            Message introduced by user: {message}
            User's email: {email}
        """
        send_mail(
            settings.CONTACT_FORM_SUBJECT,
            email_message,
            settings.CONTACT_FORM_FROM,
            settings.CONTACT_FORM_TO,
            fail_silently=False,
        )
