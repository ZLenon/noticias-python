from django import forms
from .models import News, Categories, Users

formulario = forms.ModelForm


class FormCategories(formulario):
    name = forms.CharField(max_length=200, label="Nome")

    class Meta:
        model = Categories
        fields = ["name"]


class FormNews(formulario):
    title = forms.CharField(max_length=300, label="Título")
    author = forms.ModelChoiceField(
        queryset=Users.objects.all(), label="Autoria"
    )
    content = forms.CharField(widget=forms.Textarea, label="Conteúdo")
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Criado em"
    )
    image = forms.ImageField(label="URL da Imagem")

    class Meta:
        model = News
        fields = ["title", "author", "content", "created_at", "image"]
