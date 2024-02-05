from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from party_app.forms import PartyForm


def index(request):
    return render(request, 'party_app/index.html')


@login_required
def create_party(request):
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.user = request.user
            party.save()
            return redirect(f'{party.url}')  # Redirect to a success page after successful form submission
    else:
        form = PartyForm()

    return render(request, 'party_app/create_party.html', {'form': form})
