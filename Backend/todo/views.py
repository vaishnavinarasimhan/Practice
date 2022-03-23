from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
# from glob2 import glob
from glob import *
# from todo.forms import ImageForm
# Create your views here.
# from .models import MultipleImage

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# def index(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         for file in request.FILES.getlist('images'):
#             form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form':form, 'img_obj':img_obj})

# def upload(request):
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             MultipleImage.objects.create(images=image)
#     images = MultipleImage.objects.all()
#     return render(request, 'index.html', {'images':images})

images = []
g = glob.glob("C:/Users/Anjan/Desktop/Django_Project/first_project/static/images")
for f in g:
    images.append(np.array(Image.open(f)))
images = np.array(images)