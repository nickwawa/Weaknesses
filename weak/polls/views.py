from django.shortcuts import render


def index(request):
    data = {
        'title': 'Weaknesses',
        'values': ['Love', 'Wtf', 'one'],
        'obj': {
            'Chevy': 'Punk',
            'dollars': '10,000',
            'owner': 'Rock'
        }
    }
    return render(request, 'polls/index.html', data)


def about(request):
    return render(request, 'polls/about.html')


def begin(request):
    return render(request, 'polls/begin.html')

def frnds(request):
    return render(request, 'polls/frnds.html')

