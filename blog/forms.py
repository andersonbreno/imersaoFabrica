from django.forms import ModelForm
from .models import Postagem

class FormularioPostagem(ModelForm):

    class Meta:
        model = Postagem
        fields = ['titulo','sobre', 'conteudo', 'categoria', 'observacoes', 'email']

        # trazer os atributos/tabelas do models para cá