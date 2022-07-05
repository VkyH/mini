import re
from tkinter.tix import Tree
from django.shortcuts import redirect, render
from . models import CVmodel
import cv2
from . forms import CVform
# Create your views here.

def fd(path):
    face_cascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')
    img = cv2.imread(f'static/imgfolder/{path}')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    # print(type(face_cascade))

    for (x, y , w ,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    #cv2.imshow('img',img)
    if len(faces)==0:
        # return False
        # print(faces)
        return False
        #False is a signature by default
    else:
        # return True
        # print(faces)
        return True
        #True is a photo    
    #cv2.waitKey()



    
def home(request):
    form=CVform()
    if request.method == 'POST':
        form=CVform(request.POST,request.FILES)
        
        if form.is_valid():
            personalPhoto=request.FILES.get('personalPhoto')
            sign=request.FILES.get('signaturePhoto')
            # personalPhoto=cv2.imread()
            # print(personalPhoto)
            # print(str(personalPhoto))
            # print(type(personalPhoto))
            # personalPhoto=cv2.imread()
            # print(personalPhoto)
            # print(sign)
            form.save()
            print(fd(str(sign)))
            print(fd(str(personalPhoto)))
            
            return redirect('home')
    context={'form':form,}
    return render(request, 'App/home.html',context)



# def home(request):
#     form=CVform()
#     if request.method == 'POST':
#         form=CVform(request.POST,request.FILES)
        
#         if form.is_valid():
#             personalPhoto=request.FILES.get('personalPhoto')
#             sign=request.FILES.get('signaturePhoto')
#             # personalPhoto=cv2.imread()
#             # print(personalPhoto)
#             # print(str(personalPhoto))
#             # print(type(personalPhoto))
#             # personalPhoto=cv2.imread()
#             # print(personalPhoto)

#             print(fd(str(personalPhoto)))
#             print(fd(str(sign)))
#             tempform=form.save(commit=False)
#             if not fd(str(personalPhoto)) and fd(str(sign)):
#                 temp=personalPhoto
#                 personalPhoto=sign
#                 sign=temp
#             tempform.personalPhoto=personalPhoto
#             # print(str(form.personalPhoto))
#             # print(str(form.sign))
#             tempform.sign=sign
#             # print(str(form.sign))
#             tempform.save()
#             print(fd(str(personalPhoto)))
#             print(fd(str(sign)))
#             # print(sign)
            
            
#             return redirect('home')
#     context={'form':form,}
#     return render(request, 'App/home.html',context)