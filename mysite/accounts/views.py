from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    """Регистрация пользователя"""

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
