from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm

class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

def success(request):
    return HttpResponse('Сообщение отправлено')

def index(request):
    return render(request, 'mainapp/homepage.html')

#def get_name(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
#        form = ContactForm(request.POST)
        # check whether it's valid:
#        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
#            return HttpResponse('/thanks/')

    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = ContactForm()

#    return render(request, 'wrapper.html', {'form': form})
