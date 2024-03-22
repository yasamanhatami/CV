from django.shortcuts import render
from django.http import HttpResponse
def index_views (request):
    context = {'Birthday':'16 Octuber 2008',
               'Website':'www.example.com',
               'Phone':'+123 456 7890',
               'City':'kerman,Iran',
               'Age':'15',
               'Degree':'student',
               'PhEmailone':'yasamanhatami1387@gmail.com',
               'Language':'English,Persian'}
    return render(request,'website/index.html',context)



# Create your views here.
