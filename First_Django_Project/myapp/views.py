from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Users, ToDoList, Item, ButcherNBlackbird
from .templates.forms import CreateNewList, CreateNewItem


def base(request):
    return render(request, "base.html")

def base_bootstrap(request):
    return render(request, "base_bootstrap.html")

def home(request):
    my_dict = {"1": "birinci", "2": "ikinci", "3": "üçüncü", "4": "dördüncü"}
    numbers = ["1", "2", "3", "4"]
    return render(request, "home.html", {"data": my_dict, "numbers": numbers})
    # return HttpResponse("This is how an Http Response looks like!")

def users(request):
    users = Users.objects.all()
    return render(request, "users.html", {"users": users})

def todos(response):
    items = ToDoList.objects.all()
    if response.method == "POST":
        val = response.POST.get("btn")
        return HttpResponseRedirect(f"{val}")

    return render(response, "todos.html", {})

def index(response, id):
    try:
        ls = ToDoList.objects.get(id=id)
        if response.method == "POST":
            if response.POST.get("save"):
                text = response.POST.get("new")
                if text != "":
                    ls.item_set.create(text=text, complete=False)
                    return HttpResponseRedirect(f"/todos/{id}")
                for item in ls.item_set.all():
                    if response.POST.get(f"c{item.id}") == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    new_text = response.POST.get(f"t{item.id}")
                    item.text = new_text
                    
                    item.save()

            elif response.POST.get("newItem"):
                return HttpResponseRedirect(f"/todos/{id}/create-item")
            
            elif response.POST.get("todo"):
                todo_id = response.POST.get("todo")
                return HttpResponseRedirect(f"/todos/{id}/{todo_id}")
            
        return render(response, "list.html", {"ls": ls})
    except:
        return HttpResponse("<h1>There is no ToDo List under this id!</h1>")

def item(response, id, item_id):
    try:
        todo = ToDoList.objects.get(id=id)
        item = Item.objects.get(todolist=todo, id=item_id)
        done = ("You have done this!" if item.complete else "<b>It is still waiting for you!</b>")
        return HttpResponse(f"<h1>{item.text}</h1><br></br>{done}")
    except:
        return HttpResponse("<h1>There is no item under this id!</h1>")

def create_todoList(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            list_name = form.cleaned_data["list_name"]
            t = ToDoList(name=list_name)
            t.save()
            response.user.todolist_set.add(t)
            return HttpResponseRedirect("/todos/")
    else:
        form = CreateNewList()
    return render(response, "create.html", {"form":form})

def create_item(response, id):
    if response.method == "POST":
        print("BURADAYIZZZZZ")
        form = CreateNewItem(response.POST)
        if form.is_valid():
            todo = ToDoList.objects.get(id=id)
            n = form.cleaned_data["name"] # This uncripts the data
            c = form.cleaned_data["check"]
            t = Item(todolist=todo, text=n, complete=c)
            t.save()
            return HttpResponseRedirect(f"/todos/{id}")
    else:
        form = CreateNewItem()
    return render(response, "create.html", {"form": form})

def me(response):
    how_many = ButcherNBlackbird.objects.get(id=1)
    if response.method == "POST":
        if response.POST.get("start"):
            t = response.POST.get("times")
            w = response.POST.get("was_at")
            how_many.times = t
            how_many.was_at = w
            how_many.save()

            book = "https://spread.epub.pub/epub/64dd74c1dd2f9e7246a71012"
            times = int(how_many.times)

            import pyautogui, pyperclip, time
            pyautogui.hotkey("ctrl", "t")
            pyperclip.copy(book)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("Enter")

            time.sleep(0.5)

            pyautogui.moveTo(418, 152)
            pyautogui.click()

            time.sleep(0.2)

            for i in range(times + 8):
                pyautogui.press("Tab")
            
            pyautogui.press("Enter")
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press("f11")
            pyautogui.moveTo(1500, 30)
            pyautogui.click()
            pyautogui.moveTo(1919, 1079)

    return render(response, "me.html", {"how_many": how_many})
        