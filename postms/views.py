from django.shortcuts import render

def handler400(request):
    return render(request, "400.html", status=400)

def handler403(request):
    return render(request, "400.html", status=403)

def handler404(request):
    return render(request, "400.html", status=404)

def handler404(request):
    return render(request, "400.html", status=404)
