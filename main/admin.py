from django.contrib import admin
from .models import Category, Language, Short, Word, NotWord
from modeltranslation.admin import TranslationAdmin


# admin.site.register(Category)
# admin.site.register(Language)
# admin.site.register(Short)
# admin.site.register(Word)


@admin.register(Word)
class WordAdmin(TranslationAdmin):
    list_display = ('id', 'short', 'language', 'context', 'get_categories')
    list_display_links = ('id', 'short', 'language', 'context')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }


@admin.register(Language)
class LanguageAdmin(TranslationAdmin):
    list_display = ('id', 'language')
    list_display_links = ('id', 'language')

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }


@admin.register(Short)
class ShortAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')


admin.site.register(NotWord)
