from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from party_app.models import Party


@login_required
def video_play(request, uuid):
    party = get_object_or_404(Party, uuid=uuid)
    return render(request, 'vid/video.html', {"party": party})
