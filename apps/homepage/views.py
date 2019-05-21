from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def chrats(request):
    return render(request, 'graficos.html', {})

def home(request):
    # return render(request, 'pages/home.html', {})
    valores = [['Menos de 15 días', 3251593],
               ['15 días', 1642800],
               ['30 días', 825764],
               ['45 días', 471582],
               ['60 días', 88626],
               ['75 días', 80562],
               ['90 días', 62976],
               ['105 días', 120651],
               ['120 días', 179000],
               ['135 días', 1],
    ]

    context = {'values': valores}
    template = 'charts.html'
    return render(request, template, context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'users/profile.html')
