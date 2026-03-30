from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Yil, Juri, Yarismaci
from .templates.forms import YilEkle, JuriEkle, YarismaciEkle, JuriyeYarismaciEkle


juri_resimleri = {"Murat Boz": "https://media-cdn.t24.com.tr/media/library/2019/03/1551588812998-oqvvhxzf-kmwvll-gj-7-on-ba.jpg",
                  "Ebru Gündeş": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI_aC8vyqi6LjMXC6O93rVldsjTOX6Wj2ORA&s",
                  "Beyazıt Öztürk": "https://cdn1.ntv.com.tr/gorsel/8xkQvV5ueUWL7u5uyjc6Dw.jpg?width=952&height=540&mode=both&scale=both",
                  "Oğuzhan Koç": "https://i.ytimg.com/vi/jnCAOcjIJu4/maxresdefault.jpg",
                  "Acun Ilıcalı": "https://i.ytimg.com/vi/NEmLMBVv88E/maxresdefault.jpg",
                  "Meryem Uzerli": "https://cdn.karar.com/other/2024/01/16/meerywn.jpg",
                  "Melike Şahin": "https://cdn1.ntv.com.tr/gorsel/U5lMxGfY70Gz0b1R4YkTzA.jpg?width=960&mode=crop&scale=both",
                  "Hadise": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiEVNr7K8Qoqv4tkLZeewjylmfmon_dcjflA&s",
                  "Gökhan Özoğuz": "https://img.internethaber.com/rcman/Cw480h270q95gc/storage/files/images/2019/11/03/ahmet-ahakan-athena-gokhan-vOQI_cover.jpg"}

def o_ses(response):
    yillar = Yil.objects.all()
    if response.method == "POST":
        if response.POST.get("yeni"):
            return HttpResponseRedirect("/o_ses_turkiye/sezon_ekle")
        
        elif response.POST.get("yil"):
            yil = response.POST.get("yil")
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil.replace(" ", "_")}_juriler")

    return render(response, "yillar.html", {"yillar": yillar})

def juriler(response, yil):
    sezon = Yil.objects.get(yil=yil.replace("_", " "))
    if response.method == "POST":
        if response.POST.get("ekle"):
            form = YarismaciEkle(response.POST)
            if form.is_valid():
                y = form.cleaned_data["yarismaci"]
                juriler = dict(YarismaciEkle.juriler)
                j = juriler.get(form.cleaned_data["juri"])
                if j != "":
                    eklenecek_juri = Juri.objects.get(yil=sezon, name=j.replace("_", " "))
                    yarismaci = Yarismaci(juri=eklenecek_juri, name=y)
                    yarismaci.save()
                form = YarismaciEkle()
                return render(response, "juriler.html", {"yil": sezon, "form": form})
                
        elif response.POST.get("geri"):
            return HttpResponseRedirect(f"/o_ses_turkiye")
        elif response.POST.get("juri_ekle"):
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil}_juriler/juri_ekle")
        elif response.POST.get("juri"):
            juri = response.POST.get("juri")
            return HttpResponseRedirect(f"{juri.replace(" ", "_")}")
        
    form = YarismaciEkle()
    return render(response, "juriler.html", {"yil": sezon, "form": form})

def juri_ekle(response, yil):
    sezon = Yil.objects.get(yil=yil.replace("_", " "))
    if response.method == "POST":
        form = JuriEkle(response.POST)
        if form.is_valid():
            name = form.cleaned_data["juri"]
            url = form.cleaned_data["resim"]
            yeni_juri = Juri(yil=sezon, name=name, resim=url)
            yeni_juri.save()
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil}_juriler")
    else:
        form = JuriEkle()
    return render(response, "yeni_juri.html", {"form":form, "yil":sezon})

def sezon_ekle(response):
    if response.method == "POST":
        form = YilEkle(response.POST)
        if form.is_valid():
            yil = form.cleaned_data["yil"]
            yeni_yil = Yil(yil=yil)
            yeni_yil.save()
            return HttpResponseRedirect("/o_ses_turkiye/")
    else:
        form = YilEkle()
    return render(response, "yeni_sezon.html", {"form":form})

def juri(response, yil, juri):
    sezon = Yil.objects.get(yil=yil.replace("_", " "))
    yarismacilar = Juri.objects.get(yil=sezon, name=juri.replace("_", " "))
    if response.method == "POST":
        if response.POST.get("yarismaci_ekle"):
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil}_juriler/{yarismacilar.name.replace(" ", "_")}/yarismaci_ekle")
        elif response.POST.get("geri"):
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil}_juriler")

    return render(response, "juri.html", {"yarismacilar": yarismacilar, "yil": sezon.yil})

def yarismaci_ekle(response, yil, juri):
    sezon = Yil.objects.get(yil=yil.replace("_", " "))
    j = Juri.objects.get(yil=sezon, name=juri.replace("_", " "))
    if response.method == "POST":
        form = JuriyeYarismaciEkle(response.POST)
        if form.is_valid():
            name = form.cleaned_data["yarismaci"]
            yeni_yarismaci = Yarismaci(juri=j, name=name)
            yeni_yarismaci.save()
            return HttpResponseRedirect(f"/o_ses_turkiye/{yil}_juriler/{juri}")
    else:
        form = YarismaciEkle()
    return render(response, "yeni_yarismaci.html", {"form": form, "juri": juri})
