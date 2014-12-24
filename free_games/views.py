
# Create your views here.
from django.views import generic
from free_games.models import Game
import logging
import json
from django.core import serializers

from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'free_games/index.html'
    context_object_name = 'latest_games_list'

    def get_queryset(self):
        """Return the last five added games."""
        games = Game.objects.order_by('-pub_date')[:5]
        logger.info("games = " + str(games))
        return games


class DetailView(generic.DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'free_games/detail.html'


def get_free_games(request):
    all_games = Game.objects.all()
    data = serializers.serialize("json", all_games)
    logger.info("all games = " + str(data))
    return HttpResponse(data)
