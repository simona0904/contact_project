from django.views.generic import FormView
from contacts.forms import ContactForm
from django.contrib import messages

# Create your views here.

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contacts/form.html'
    success_url = '/'

    def form_valid(self, form: ContactForm):
        form.send_mail()
        messages.success(self.request, "Message successfully sent. Thank you for contacting us.")
        return super().form_valid(form)       # super face redirect la succes url


