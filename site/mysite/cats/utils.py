from django.db.models import Count

from .models import Category

menu = [
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('cat'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['categories'] = categories
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
