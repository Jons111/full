from django.shortcuts import render
from myfiles.models import Murojat
import requests
# Create your views here.
def murojat(request):
    m = Murojat.objects.all()
    return render(request,'index.html',{'max':m})
def habar(request,idd):
    m = Murojat.objects.get(id =idd)
    bot_token = '5252380798:AAHrim6pd7XaNsXJ5dWlk9sqosL_yVchtf4'
    chat_id = m.tg_id
    if request.method =='POST':

        text  = request.POST.get('habar')
        d = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}'
        print(d)
        # render()
        requests.get(d)
        m = Murojat.objects.get(id=idd).delete()
        m = Murojat.objects.all()
        return render(request, 'index.html', {'max': m})
    else:
        return render(request,'habar.html',{'habar':m})