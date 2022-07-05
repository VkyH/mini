from django.conf import Settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import minimg
import numpy as np
from PIL import Image
import cv2
from base64 import b64encode
from .forms import FileForm
# Create your views here.
def fd(imageArr):
    # imgobj=minimg.objects.get( personalPhoto=image)
    # print(imgobj)
    # print(img.personalPhoto)
    # print(type(img.personalPhoto))
    
    
    # imgg = Image.open(imgobj.personalPhoto)
    # img = np.array(imgg) 
    # print(img)
    
    img=imageArr
    # imgg = Image.open(image)
    face_cascade = cv2.CascadeClassifier('miniApp/haarcascade_frontalface_default.xml')
    print(face_cascade)
    # img = cv2.imread(image)
    # img=np.array(img)
    # img=cv2.imread('')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    #cv2.imshow('img',img)
    if len(faces)==0:
        # return False
        print(faces)
        #False is a signature by default
    else:
        # return True
        print(faces)
        #True is a photo    
    #cv2.waitKey()

# fd('miniApp/sig.png')


def home(request):
    if request.method=='POST':
        fname=request.POST.get('studentName')
        # dob=request.POST.get('studentdob')
        # gender=request.POST.get('studentgender')
        # categ=request.POST.get('studentcat')
        # email=request.POST.get('studentemail')
        # phno=request.POST.get('studentpnumber')
        # address=request.POST.get('studentaddress')
        personalPhoto= request.FILES['personalPhoto']
        print(type(personalPhoto))
        # print(fname,dob,gender,categ,email,phno,address)
        print(fd(personalPhoto))
    return render(request, 'miniApp/index.html')

# def imgdisplay(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = request.FILES['personalPhoto',False]
#             form = FileForm()
#             context = {'form': form, 'image': image}
#             return render(request, 'miniApp/home.html', context)
#     else:
#         form = FileForm()
#     return render(request, 'miniApp/home.html', {'form': form})


def temp(request):
    img=minimg.objects.get( personalPhoto='black_leopard.jpg')
    # print(img.personalPhoto)
    # print(type(img.personalPhoto))
    # imgg = Image.open(img.personalPhoto)
    imgg = Image.open(r'C:\Users\vky_h\Desktop\mini\miniProject\public\static\black_leopard.jpg')
    imgArray = np.array(imgg)
    print(type(imgArray))
    # image=cv2.imread(img.personalPhoto)
    # print(image)
    fd(imgArray)
    return HttpResponse('hello')
    