from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from users import models
from users.models import Profile
from .forms import WeightForm

def home(request):
    form = WeightForm()
    if request.is_ajax():
        #profile = get_object_or_404(Profile, id = request.user.id)
        form = WeightForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return JsonResponse({
                'msg': 'Success'
            })
        
    return render(request, 'Landing/index.html',{'form':form})

def get_data(request, *args,**kwargs):
        dates_queryset = Profile.objects.all().filter(user = request.user)
        dates = list(dates_queryset.values_list('date', flat=True))
        weights = list(dates_queryset.values_list('weight', flat=True))

        profile = Profile.objects.filter(user = request.user).latest('id')
        bmiCalc = profile.weight / (profile.height*profile.height)
        Profile.objects.filter(user=request.user).update(bmi=bmiCalc)
        bmi = bmiCalc*10000
        status = ""

        if bmi < 16:
            status = "Severe Thinness"
        elif bmi > 16 and bmi < 17:
            status = "Moderate Thinness"
        elif bmi > 17 and bmi < 18:
            status = "Mild Thinness"
        elif bmi > 18 and bmi < 25:
            status = "Normal"
        elif bmi > 25 and bmi < 30:
            status = "Overweight"
        elif bmi > 30 and bmi < 35:
            status = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            status = "Obese Class II"
        elif bmi > 40:
            status = "Obese Class III"
       


        data = {
            'date':  dates,
            'weight':  weights,
            'bmi': bmi,
            'status': status,
            'msg': 'new'
            
        }
        return JsonResponse(data, safe=False)
   
