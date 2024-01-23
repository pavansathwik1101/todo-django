from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member

# Create your views here.
def index(request):
    member=Member.objects.all().values()
    context={'member':member}
    return render(request,'index.html',context)
def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        member = Member(name=name)
        member.save()

        return redirect('index')  # Redirect to the index page after adding a member

    return render(request, 'index.html')


def delete_member(request,member_id):
    member=Member.objects.get(id=member_id)
    member.delete()
    return redirect('index')
