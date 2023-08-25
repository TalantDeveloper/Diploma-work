
from .models import Word, Category, Language
from modeltranslation.translator import TranslationOptions, register


@register(Word)
class WordTranslationOptions(TranslationOptions):
    fields = ['context', 'description']


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ['language']
