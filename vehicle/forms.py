from django import forms
from .models import PostsSubmit
#from django.forms import ModelForm
class PostsSubmitForm(forms.ModelForm):
	class Meta:
		model = PostsSubmit
		fields = ("vehicle_no", "type","vehicle_image")
		
		
	
