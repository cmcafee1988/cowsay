from django.shortcuts import render
from cowsay_app.models import User_Input
from cowsay_app.forms import User_Input_Form
import subprocess


# Create your views here.
def index_view(request):
    cowsays = ""
    if request.method == "POST":
        form = User_Input_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User_Input.objects.create(text=data.get("text"))
            text = data.get("text")
            cowsays = subprocess.check_output(["cowsay", text], text=True)
            form = User_Input_Form()
            return render(request,
                          'index.html',
                          {
                              "title": "The Kenzie Academy HTTP, Forms, and Cows assessment",
                              "form": form,
                              "cowsays": cowsays,
                          }
                          )


    form = User_Input_Form()
    return render(
        request,
        "index.html",
        {
            "title": "The Kenzie Academy HTTP, Forms, and Cows assessment",
            "form": form,
            "cowsays": cowsays,
        }
    )


def cowsay_show_view(request):
    cowsay_topten = User_Input.objects.order_by("-id")[:10]
    return render(request, "cowsay_show.html", {"title": "The Last 10 phrases from the Kenzie Academy HTTP, Forms, and Cows assessment", "data": cowsay_topten})


# Create your views here.
