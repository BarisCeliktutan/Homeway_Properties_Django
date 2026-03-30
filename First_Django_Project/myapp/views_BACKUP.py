from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import TodoItem, Users
from .templates.forms import CreateNewList

# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")
    # return HttpResponse("This is how an Http Response looks like!")

def todos(response):
    items = TodoItem.objects.all()
    if response.method == "POST":
        if response.POST.get("save"):  # The name of "Save" button
            for item in items:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()

        elif response.POST.get("newItem"):  # The name of "Add To Do" button
            pass

    return render(response, "todos.html", {"todos": items})

def users(request):
    users = Users.objects.all()
    return render(request, "users.html", {"users": users})

def index(response, id):
    try:
        item = TodoItem.objects.get(id=id)
        done = ("You have done this!" if item.completed else "<b>It is still waiting for you!</b>")
        return HttpResponse(f"<h1>{item.title}</h1><br></br>{done}")
    except:
        return HttpResponse("<h1>There is no item under this id!</h1>")
    
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"] # This uncripts the data
            c = form.cleaned_data["check"]
            t = TodoItem(title=n, completed=c)
            t.save()
            return HttpResponseRedirect("/todos/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "create.html", {"form": form})

def me(response):
    return HttpResponse("<h1>Barış Çeliktutan</h1>\n<h3>Software Engineer (to be...)</h3>")