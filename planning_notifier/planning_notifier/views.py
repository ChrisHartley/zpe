from django.shortcuts import render

def homepage(request):
    context = {
        'title': 'Homepage',
        'hello': 'Goodbye ZPE',
        'svelteProps': {
          'hello': 'Goodbye Svelte',   
        }
    }
    return render(request, 'index.html', context)