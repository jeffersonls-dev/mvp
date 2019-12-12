from django import forms
from .models import Livro
#DataFlair
class LivroCreate(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
