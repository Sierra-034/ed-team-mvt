from django.shortcuts import render

# Create your views here.
def index(request):
    lista_articulos = [
        {
            'titulo': 'Mover, copiar y renombrar directorios en linux',
            'imagen': 'https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2F511e1605-3a2a-46ba-a211-ff5d33d6028f.png&w=1920&q=75',
            'autor': 'Alvaro Felipe Chávez',
        },
        {
            'titulo': 'Sistemas Binarios y Decimales',
            'imagen': 'https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2Fb412d87c-b524-49e3-93ff-403fe79b1f54&w=1920&q=75',
            'autor': 'Amanda Silva',
        },
        {
            'titulo': 'Normalización de Bases de Datos',
            'imagen': 'https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2F965780b1-7a4c-442c-8fe8-53d5e913da95.png&w=1920&q=75',
            'autor': 'John Díaz',
        },
    ]

    context = {
        'articulos': lista_articulos
    }
    return render(request, 'index.html', context)
