from django import forms

class YilEkle(forms.Form):
    yil = forms.CharField(label="Yıl", max_length=200)

class JuriEkle(forms.Form):
    juri = forms.CharField(label="Jüri Adı", max_length=200)
    resim = forms.URLField(label="Resim URL'si", max_length=500)

    # password = forms.CharField(widget=forms.PasswordInput())
    
class JuriyeYarismaciEkle(forms.Form):
    yarismaci = forms.CharField(label="Yarışmacı Adı", max_length=200)

class YarismaciEkle(forms.Form):
    yarismaci = forms.CharField(label="Yarışmacı Adı", max_length=200, required=False)

    juriler = (
        ("1", ""),
        ("2", "Murat Boz"),
        ("3", "Ebru Gündeş"),
        ("4", "Beyazıt Öztürk"),
        ("5 ", "Oğuzhan Koç"),
    ) 
    juri = forms.ChoiceField(choices=juriler)
