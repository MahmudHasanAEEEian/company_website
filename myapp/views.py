from django.shortcuts import render
from django.http import JsonResponse
from .models import SendMessage
from .forms import SendMessageForm

# Create your views here.
#home page will be rendered here.
def index(request):
    context = {
        'name': 'Md. Mahmud Hasan'
    }
    return render(request, 'index.html', context)

#about page will be rendered here.
def about_us(request):
    context = {
        'message':'This is About page.'
    }
    return render(request, 'about/about.html', context)


#service page will be rendered here.
def company_services(request):
    context = {
        'message':'This is service page.'
    }
    return render(request, 'services/services.html', context)


#contact form for sending messages to a specific address
def send_message(request):
    messages = SendMessage.objects.all()
    context ={
        'messages': messages
    }
    
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()    
    return render(request, 'contact/contact.html', context)