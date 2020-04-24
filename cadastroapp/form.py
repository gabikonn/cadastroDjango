from django.forms import ModelForm
from cadastroapp.models import novoCadastro

class CadastroForm(ModelForm):
    class Meta:
        model = novoCadastro
        fields = ['nome', 'altura', 'dataNasc']
