from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST" and request.FILES['file'] and request.FILES['file2'] and 'key' in request.POST:
        python_file_path = "./route.py"
        exec(open(python_file_path).read())
        return render(request, "home.html")
    else:
        return render(request, "home.html")