from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # differ between request.POST and request.POST.get
    # link: https://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference
    # using request.POST.get
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text', ''),
    # })

    # using request.POST
    if 'item_text' in request.POST:
        return render(request, 'home.html', {
            'new_item_text': request.POST['item_text'],
        })
    else:
        return render(request, 'home.html', {
            'new_item_text': '',
        })

