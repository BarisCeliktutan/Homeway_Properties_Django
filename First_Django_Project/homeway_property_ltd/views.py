from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import Flat, Maintenance_Notes, Cleaner
from .templates.forms import NewFlat, NewCleaner, Maintenance_Note

flat_photos = {"1, 102 Upper Street": "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTM3NzQ2ODMxMjYyMzcwMTA4NA==/original/7b528f3d-f205-4f48-b27d-eb08413122ac.jpeg?im_w=1200",
               "3, 102 Upper Street": "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTM4OTAwODEyMzA0Njg0OTg0NA==/original/05658f96-47f4-4456-bdc2-e09f8416b362.jpeg?im_w=1440",
               }

# Create your views here.
def homeway(response):
    flats = Flat.objects.all()
    if response.method == "POST":
        if response.POST.get("add_flat"):
            return HttpResponseRedirect("/homeway_property_ltd/add_new_flat")
        
        elif response.POST.get("cleaners"):
            return HttpResponseRedirect("/homeway_property_ltd/cleaners")
        
        elif response.POST.get("flat"):
            flat = response.POST.get("flat")
            return HttpResponseRedirect(f"{flat.replace(" ", "_")}")
        
        elif response.POST.get("schedule"):
            return HttpResponseRedirect("/homeway_property_ltd/schedule")


    return render(response, "flats.html", {"flats": flats, "flat_photos": flat_photos})

def add_flat(response):
    if response.method == "POST":
        form = NewFlat(response.POST)
        if form.is_valid():
            if response.POST.get("save"):
                flat_no = form.cleaned_data["flat_no"]
                building = form.cleaned_data["building"]
                post_code = form.cleaned_data["post_code"]
                kingsize_beds = form.cleaned_data["kingsize_beds"]
                double_beds = form.cleaned_data["double_beds"]
                sofa_beds = form.cleaned_data["sofa_beds"]
                url = form.cleaned_data["photo_url"]

                new_flat = Flat(flat_no=flat_no, building=building, post_code=post_code, kingsize_beds=kingsize_beds,
                                double_beds=double_beds, sofa_beds=sofa_beds, photo_url=url)
                new_flat.save()

            return HttpResponseRedirect("/homeway_property_ltd")
    else:
        form = NewFlat()
    return render(response, "add_flat.html", {"form": form})

def flat_details(response, flat_no, building):
    flat = Flat.objects.get(flat_no=flat_no, building=building.replace("_", " "))
    try:
        notes = Maintenance_Notes.objects.get(flat=flat)
    except:
        notes = None

    if response.POST.get("back"):
        return HttpResponseRedirect("/homeway_property_ltd")
    elif response.POST.get("maintenance"):
        return HttpResponseRedirect(f"{flat_no}-{building.replace(" ", "_")}/add_maintenance_note")
    elif response.POST.get("edit_note"):
        note_id = response.POST.get("edit_note")
        return HttpResponseRedirect(f"{flat_no}-{building.replace(" ", "_")}/edit_maintenance_note_{note_id}")

    return render(response, "flat_details.html", {"flat": flat, "maintenance_notes": notes})

def cleaners(response):
    cleaners = Cleaner.objects.all()
    if response.POST.get("add_cleaner"):
            return HttpResponseRedirect("add_new_cleaner")
    elif response.POST.get("back"):
            return HttpResponseRedirect("/homeway_property_ltd")
    return render(response, "cleaners.html", {"cleaners": cleaners})

def add_cleaner(response):
    if response.method == "POST":
        form = NewCleaner(response.POST)
        if form.is_valid():
            if response.POST.get("save"):
                name = form.cleaned_data["name"]

                new_cleaner = Cleaner(name=name)

                new_cleaner.save()
            return HttpResponseRedirect("/homeway_property_ltd/cleaners")
    else:
        form = NewCleaner()

    return render(response, "add_cleaner.html", {"form": form})

def add_edit_maintenance_note(response, flat_no, building, note_id=None):
    flat = Flat.objects.get(flat_no=flat_no, building=building.replace("_", " "))

    if note_id:
        n = get_object_or_404(Maintenance_Notes, id=note_id)
    else:
        n = None
    
    if response.method == "POST":
        form = Maintenance_Note(response.POST, instance=n)
        if form.is_valid():
            if response.POST.get("save"):
                if n:
                    n.save()
                else:
                    note = form.cleaned_data["note"]
                    done = form.cleaned_data["done"]
                    
                    new_note = Maintenance_Notes(flat=flat, note=note, done=done)

                    new_note.save()

            return HttpResponseRedirect(f"/homeway_property_ltd/{flat_no}-{building.replace(" ", "_")}")
    else:
        form = Maintenance_Note(instance=n)

    return render(response, "add_maintenance_note.html", {"form": form, "flat": flat})

def schedule(response):
    return render(response, "cleaning_schedule .html")
