from django import forms
from ..models import Maintenance_Notes

class NewFlat(forms.Form):
    flat_no = forms.CharField(label="Flat No", max_length=50, required=False)
    building = forms.CharField(label="Building Name", max_length = 300, required=False)
    post_code = forms.CharField(label="Post Code", max_length=50, required=False)

    kingsize_beds = forms.CharField(label="Number of King Size Beds", max_length=50, required=False)
    double_beds = forms.CharField(label="Number of Double Beds", max_length=50, required=False)
    sofa_beds = forms.CharField(label="Number of Sofa beds", max_length=50, required=False)

    photo_url = forms.URLField(label="Photo URL", max_length=10000, required=False)

# class Maintenance_Note(forms.Form):
#     note = forms.CharField(widget=forms.Textarea(attrs={"rows":"6", "cols":"100"}), max_length=10000, required=False)
#     done = forms.BooleanField(required=False)

class Maintenance_Note(forms.ModelForm):
    class Meta:
        model = Maintenance_Notes
        fields = ["note", "done"]
    
class NewCleaner(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=False)
