from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'placeholder':'Escribe tu nombre'}) )
    email=forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'placeholder':'Escribe tu email'}))
    content=forms.CharField(label="Contenido", required=True, widget=forms.Textarea(attrs={'placeholder':'Escribe tu mensaje'}))