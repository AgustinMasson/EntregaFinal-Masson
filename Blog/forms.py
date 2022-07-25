from django import forms


class PostBlog(forms.Form):

    titulo = forms.CharField(label="Title")
    cuerpo = forms.CharField(label="Body")
    autor = forms.CharField(label="Author")
    fecha = forms.CharField(label="Date")
    equipo = forms.CharField(label="Team/s Involved")
    jugador_actual = forms.CharField(label="Player/s Involved")