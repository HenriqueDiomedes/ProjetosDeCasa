from django.shortcuts import render

# Create your views here.
def formulario(request):
    dialogo = request.GET.get('dialogo')

    print("dialogo", dialogo)

    context = {
        'dialogo':dialogo
    }

    return render(request, 'formulario.html', context)

def card(request):
  
    return render(request, 'card.html')