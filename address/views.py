from django.http import HttpResponse
from django.shortcuts import render
from addressnet.predict import predict_one

def index(request):
    print(predict_one("casa del gelato, 10A 24-26 high street road mount waverley vic 3183"))
    # return render(request, 'address/index.html')
    return HttpResponse("Hello, world. You're at the  index.")
