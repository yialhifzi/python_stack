from django.shortcuts import render, redirect, HttpResponse


def root(request):
    return redirect("/DojoSurvey")


def index(request):
    return render(request, 'index.html')


def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    favlang_from_form = request.POST['favlang']
    comment_from_form = request.POST['comment']

    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "favlang_on_template" : favlang_from_form,
        "comment_on_template" : comment_from_form

    }
    return render(request,"result.html",context)