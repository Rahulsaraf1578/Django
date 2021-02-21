from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination

def index(request):
    ######################################################################
    # This was static data so we have to delete it
    # dest1 = Destination( )
    # dest1.name  = 'Mumbai'
    # dest1.desc = 'The city that never sleeps'
    # dest1.price = 7000
    # dest1.img = 'https://source.unsplash.com/200x250/?nature,animals'
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'New orleans'
    # dest2.desc = 'The city of lakes'
    # dest2.price = 5000
    # dest2.img = 'https://source.unsplash.com/200x250/?nature,birds'
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'France'
    # dest3.desc = 'The city of forts'
    # dest3.price = 4000
    # dest3.img = 'https://source.unsplash.com/200x250/?nature,insects'
    # dest3.offer = True
    #
    # dest4 = Destination()
    # dest4.name = 'Dheradun'
    # dest4.desc = 'The city mountain'
    # dest4.price = 3000
    # dest4.img = 'https://source.unsplash.com/200x250/?nature,mammels'
    # dest4.offer = False
    #
    # dests = [dest1,dest2,dest3,dest4]
    #######################################################################

    dests = Destination.objects.all( )

    return render(request,'index.html',{'dests':dests});

