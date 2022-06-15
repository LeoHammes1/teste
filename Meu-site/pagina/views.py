from email import message
import email
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_sub = request.POST['message-subject']
        message = request.POST['message']

        data = {
            'name':message_name,
            'email': message_email,
            'subject': message_sub,
            'message': message
        }

        message = '''
        Nova Mensagem: {}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'], message, '',['leo_hammes09@hotmail.com'])

        return render(request,'index.html', {'message_name': message_name})
    else:
        return render(request,'index.html')
   