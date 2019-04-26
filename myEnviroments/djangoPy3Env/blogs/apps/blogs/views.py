# views.py
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogs/index.html", context)

def create(request):
    if request.method == 'POST':
        request.session['name'] = "test"
        return render(request, "create.html")
    else:
        return redirect("/")
    
