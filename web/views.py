from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Publication


def index(request):
    return render(request, 'index.html')


def status(request):
    return HttpResponse('<h2>OK</h2')


messages_data = [
    {
        'name': 'Dana Darko',
        'date': datetime.now(),
        'email': 'danadarko@mail.com',
        'phone number': '123-45-11',
        'text': '''Really looking forward hearing from you'''
    },
    {
        'name': 'Frederick Falke',
        'date': datetime.now(),
        'email': 'falke@gmail.com',
        'phone number': '+43 098 777 222',
        'text': '''Wanted to discuss my project'''
    }
                    ]


publications_data = [
    {
        'id': 0,
        'name': 'What is Lorem Ipsum?',
        'date': datetime.now(),
        'text': '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
    },
    {
        'id': 1,
        'name': 'Where does it come from?',
        'date': datetime.now(),
        'text': '''Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
                    <br><br>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'''
    },
    {
        'id': 2,
        'name': 'Why do we use it?',
        'date': datetime.now(),
        'text': '''It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'''
    }
]


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = (request.POST['secret'])
        name = (request.POST['name'])
        text = (request.POST['text'])

        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'Wrong Secret Key'
            })
        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': 'Blank field'
            })
        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'No text submitted'
            })

        Publication(name=name,
                    date=datetime.now(),
                    text=text.replace('\n', '<br />')
        ).save()
        return redirect('/publications')


def publications(request):
    return render(request, 'publications.html', {
        'publications': publications_data
    })


def publication(request, number):
    if number < len(publications_data):
        return render(request, 'publication.html', publications_data[number])
    else:
        return redirect('/')


def messages(request):
    return render(request, 'messages.html', {
        'messages': messages_data
    })


def message(request, number):
    if number < len(messages_data):
        return render(request, 'message.html', messages_data[number])
    else:
        return redirect('/')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    else:
        name = (request.POST['name'])
        text = (request.POST['text'])


        if len(name) == 0:
            return render(request, 'message.html', {
                'error': 'Blank field'
            })
        if len(text) == 0:
            return render(request, 'message.html', {
                'error': 'No text submitted'
            })
        messages_data.append({
            'name': name,
            'date': datetime.now(),
            'text': text.replace('\n', '<br />')
        })
        return render(request, 'contacts.html', {
            'messages': messages_data
        })
