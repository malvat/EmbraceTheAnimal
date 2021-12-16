from django.shortcuts import render

def add_new_pet(request): 
    return render(request, 'add_new_pet.html')