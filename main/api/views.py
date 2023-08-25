from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, LanguageSerializer, ShortSerializer, WordSerializer
from ..models import Category, Language, Short, Word


class CategoryViewsSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguageViewsSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ShortViewsSet(ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer


class WordViewsSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
