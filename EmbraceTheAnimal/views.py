from django.shortcuts import redirect, render

from adoptions.models import Pet

def home(request): 
    pets = Pet.objects.all()
    if "logged_in" in request.session.keys(): 
        print(request.session['logged_in'])
        return render(request, 'home.html', {
            'logged_in': request.session['logged_in'],
            'pets': pets
        })
    else:
        return render(request, 'home.html', {
            'logged_in': False,
            'pets': pets
        })