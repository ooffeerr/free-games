

# from django.contrib import admin
# from free_games.models import Game
#
# class GameInline(admin.TabularInline):
#     model = Game
#     extra = 3
#
#
# class GameAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [GameInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#
#
# admin.site.register(Game, GameAdmin)
from django.contrib import admin
from free_games.models import Game

admin.site.register(Game)