from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewsSet, LanguageViewsSet, ShortViewsSet, WordViewsSet


router = DefaultRouter()

router.register('category', CategoryViewsSet)
router.register('language', LanguageViewsSet)
router.register('short', ShortViewsSet)
router.register('word', WordViewsSet)

urlpatterns = router.urls
