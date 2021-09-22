from django.shortcuts import render
from .models import Person, Participant, Student
from django.core import serializers
from .forms import PersonForm, ParticipantForm, StudentForm
from django.http import JsonResponse
# Create your views here.

# def displayData(request):
#     form = PersonForm()
#     person = Person.objects.all()
#     return render(request,'index.html',{'form':form})

def register_person(request):
    pass

def postParticipant(request):
    form = ParticipantForm()
    if request.method == "POST" and request.is_ajax :
        # import pdb; pdb.set_trace()
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            # instance = form.save()
            # ser_instance = serializers.serialize('json', [instance,] )
            # ser_instance = serializers.serialize('json',Participant.objects.all())
            # return JsonResponse({"instance": ser_instance}, status=200)
            fetchdata = list(Participant.objects.values())
            print(fetchdata)
            return JsonResponse({'instance':fetchdata}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return  render(request,'participantform.html',{'form':form})

def student_data(request):
    if request.method == 'GET':
        form = StudentForm()
        data = Student.objects.all()
        return render(request,'student.html',{'form':form,'s_data':data})
    elif request.method == 'POST' and request.is_ajax:
        import pdb; pdb.set_trace()
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            fetch_data = list(Student.objects.values())
            print(fetch_data)
            return JsonResponse({"student":fetch_data}, status=200)
        else:
            return JsonResponse({'error':form.errors}, status=400)