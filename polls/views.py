from django.shortcuts import render
from .forms import UserForm
from .forms import ResultForm

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        #result = Analyzer.Analyze(text)
        userformR = ResultForm(initial={'result':""})
        return render(request, "result.html", {"form": userformR})
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
