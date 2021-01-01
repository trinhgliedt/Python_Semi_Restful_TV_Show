from django.shortcuts import render, redirect
from .models import Show
from time import strftime, strptime
from django.contrib import messages
from datetime import datetime


def new_show_input(request):
    return render(request, 'addShow.html')

def create_new_show(request):
    print(request.POST)
    # print("datetime.now():", type(datetime.now().strftime('%Y-%m-%d')), datetime.now().strftime('%Y-%m-%d'))
   
    # print("datetime.datetime.now().date()", type(datetime.now().date()), datetime.now().date())

    
    # print("type of request.POST['released_date']:",type(datetime.strptime(request.POST['released_date'], "%Y-%m-%d").date()),datetime.strptime(request.POST['released_date'], "%Y-%m-%d").date())
    errors = Show.objects.basic_validator(request.POST, "Add")

    if len(errors) > 0:
        # val represents the actual error string
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/shows/new")


    if request.method == "POST":
        created_show = Show.objects.create(tittle = request.POST['tittle'], network = request.POST['network'], released_date = request.POST['released_date'],description = request.POST['desc'])
        print("created_show.id: ", created_show.id)
    return redirect(f"/shows/{created_show.id}")


def display_show_info(request, show_id):
    this_show= Show.objects.get(id=show_id)
    this_show.released_date = this_show.released_date.strftime("%m/%d/%Y")
    
    context = {
            "this_show": this_show,
        }
    return render(request, 'showDetail.html', context)


def all_show(request):

    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, 'allShows.html', context)

def index(request):
    return redirect("/shows")


def edit_show_input(request, show_id):
    
    show_to_edit= Show.objects.get(id=show_id)
    show_to_edit.released_date = show_to_edit.released_date.strftime("%Y-%m-%d")
    context = {
        "show_to_edit": show_to_edit,
    }
    return render(request, 'editShow.html', context)

def make_edit(request, show_id):
    print(request.POST)
    errors = Show.objects.basic_validator(request.POST, "Edit")

    if len(errors) > 0:
        # val represents the actual error string
        for key, val in errors.items():
            messages.error(request, val)
        return redirect(f"/shows/{show_id}/edit")
    
    show_to_edit = Show.objects.get(id=show_id)
    show_to_edit.tittle = request.POST["tittle"]
    show_to_edit.network = request.POST["network"]
    show_to_edit.released_date = request.POST["released_date"]
    show_to_edit.description= request.POST["desc"]

    show_to_edit.save()

    show_id = show_to_edit.id
    
    return redirect(f"/shows/{show_id}")

def delete_show(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/shows")