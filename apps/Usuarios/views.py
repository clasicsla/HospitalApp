from django.shortcuts import render
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Users

def index(request):
    lastest_user_created = Users.objects.order_by('-created')[:5]
    template = loader.get_template('Usuarios/base.html')
    
    f = UserForm()
    usr = Users.objects.all()
    mensaje = "Inicializado"
    if request.method == 'POST':
		mensaje = 'Es POST'
		f = UserForm(request.POST)

		if f.is_valid():  
			mensaje = 'Es valido'
			f.save()
			#ArticleForm(request.POST, instance=usr)
		else:
			mensaje = 'Es invalido'
    context = {
        'lastest_users_list': lastest_user_created,
        'form':f,
        'mensaje':mensaje,
    }
    return HttpResponse(template.render(context, request))



def index2(request):
    lastest_user_created = Users.objects.order_by('-created')[:5]
    template = loader.get_template('Usuarios/base.html')
    context = {
        'lastest_users_list': lastest_user_created,
    }
    f = UserForm()
    usr = Users.objects.all()
    if usr:
    	ArticleForm(request.POST, instance=usr)
    	pass
    return HttpResponse(template.render(context, request))
