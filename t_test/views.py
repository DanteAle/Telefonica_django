from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from t_test.models import Cmts,Nodo,Troba, Usuario, TareaProgramada,InfoCore,InfoPlanta, TareaNoc
from .forms import nuevaTareaForm

# Create your views here.

def index (request):

    class NameForm(forms.Form):

        your_name = forms.CharField(label='Your name', max_length=100)
        name = forms.CharField(max_length=30)
        email = forms.EmailField(max_length=254)
        message = forms.CharField(
            max_length=2000,
            widget=forms.Textarea(),
            help_text='Write here your message!'
        )
        source = forms.CharField(       # A hidden input for internal use
            max_length=50,              # tell from which page the user sent the message
            widget=forms.HiddenInput()
        )

        #template = "your_template.html"
    #context = { "form" : NameForm() }
    tarea=TareaProgramada.objects.order_by('tareaProgramadaId')

    my_dict={'insert_me':'Vengo de don views.py', 'tarealist':tarea}
    #return HttpResponse("<b><u>Hello World</u></b>")
    return render(request,'index.html',context=my_dict)


def usuarios(request,id):


    listausuarios=Usuario.objects.filter(troba__trobaId=id)
    my_dict={'usuarioslist':listausuarios}
    return  render(request,'usuarios.html',context=my_dict)


def tareasnoc(request):


    listaTareas=TareaNoc.objects.order_by('fechaHoraInicio')
    my_dict={'tarealist':listaTareas}
    return  render(request,'tareasnoc.html',context=my_dict)

def addTarea(request):

    form = nuevaTareaForm

    if request.method=='POST':
        print('entro tu post')
        form=nuevaTareaForm(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Informacion invalida')

    return render(request,'form.html',{'form':form})
