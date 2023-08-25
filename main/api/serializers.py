
from rest_framework.serializers import ModelSerializer
from ..models import Category, Language, Short, Word


class CategorySerializer(ModelSerializer):
    """Category models serializer name CategorySerializer"""
    class Meta:
        model = Category
        fields = '__all__'
        depth = 2


class LanguageSerializer(ModelSerializer):
    """Language models serializer name LanguageSerializer"""
    class Meta:
        model = Language
        fields = '__all__'
        depth = 2


class ShortSerializer(ModelSerializer):
    """Short model serializer name ShortSerializer"""
    class Meta:
        model = Short
        fields = '__all__'
        depth = 2


class WordSerializer(ModelSerializer):
    """Word model serializer name Word Serializer"""
    class Meta:
        model = Word
        fields = '__all__'
        depth = 1
