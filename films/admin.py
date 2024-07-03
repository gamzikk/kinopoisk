from django.contrib import admin
from .models import Film, Genre, Comment, RatingMark, Rating

# admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(RatingMark)
admin.site.register(Rating)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ['genre']
    search_fields = ['name']


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     filter_horizontal = ['films']
#     search_fields = ['name']