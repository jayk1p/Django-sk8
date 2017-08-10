from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/home.html')
    # Notice that since this set of code is here,
    # The text above is not showing


def contact(request):
    return render(request, 'home/contact.html',{'content':['If you would like to contact me, please email me. at joukyuu@hotmail.com. Or you can visit my github at github.com/jayk1p', 'thanks']})


# Create your views here.
