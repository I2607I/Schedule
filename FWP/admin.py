from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'day', 'number_lesson', 'type_lesson', 'is_even', 'classroom')
    # list_display_links = ('id', 'title')
    search_fields = ('subject', 'day')
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}
    

class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'content')
    prepopulated_fields = {"slug": ("name",)}


class NumberLessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')


class TypeLessonAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ParityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(NumberLesson, NumberLessonAdmin)
admin.site.register(TypeLesson, TypeLessonAdmin)
admin.site.register(Parity, ParityAdmin)