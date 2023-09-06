from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Yoshelin Yamala Vijnana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
