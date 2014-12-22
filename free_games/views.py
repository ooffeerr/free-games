
# Create your views here.
from django.views import generic
from free_games.models import Game


class IndexView(generic.ListView):
    template_name = 'free_games/index.html'
    context_object_name = 'latest_games_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Game.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'free_games/detail.html'
