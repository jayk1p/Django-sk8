from django.shortcuts import render

def index(request):
     return render(request, 'home/tricktips.html')
    # Notice that since this set of code is here,
    # The text above is not showing
