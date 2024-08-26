from django.shortcuts import render
from shop.models import User,Abzar
# Create your views here.

def Posts(request):
    abzars = Abzar.objects.all()
    
    context = {
        "abzarha":abzars,
        }
    return render(request, "shop/posts.html",context)


def Post_details(request, post_id):
    abzars = Abzar.objects.get(pk =post_id)
    
    context = {
        "details":abzars,
        }
    return render(request, "shop/postdetails.html",context)



