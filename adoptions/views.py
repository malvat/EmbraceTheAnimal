from django.shortcuts import render

from adoptions.models import Pet
from accounts.models import AccountUser

def add_new_pet(request): 
    if request.method == "POST": 
        current_user = AccountUser.objects.get(email=request.session['user']['email'])
        tmp_pet = Pet.objects.create(
            name = request.POST['pet_name'],
            age = request.POST['age'],
            species = request.POST['species'],
            breed = request.POST['breed'],
            weight =  request.POST['weight'],
            sex = request.POST['sex'],
            hobbies = request.POST['hobbies'],
            summary = request.POST['summary'],
        )
        tmp_pet.profile_pic = request.FILES['profile_pic']
        tmp_pet.submitter.add(current_user)
        tmp_pet.save()
    return render(request, 'add_new_pet.html')