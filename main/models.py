from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """Categories Translate many language"""
    name = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return self.name


class Language(models.Model):
    """Languages Translate many language"""
    language = models.CharField(max_length=100, verbose_name='Language')

    def __str__(self):
        return self.language


class Short(models.Model):
    """Short word model."""
    name = models.CharField(max_length=200, verbose_name='Name')
    is_active = models.BooleanField(verbose_name='Is Active', default=False)

    def __str__(self):
        return self.name


class Word(models.Model):
    """Short Word context, descripton, language and categories fields"""
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='word')
    categories = models.ManyToManyField(Category, related_name='word')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='word')
    context = models.TextField(verbose_name='Context', null=True, blank=True)  # Translation field
    description = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.context

    def get_categories(self):
        """Return a list of category names and count"""
        titles = [category.name for category in self.categories.all()]
        return {'count': self.categories.all().count(), 'titles': titles}


class NotWord(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
