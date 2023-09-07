from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинация с заданными параметрами от 3-х до 20 элементов на странице"""
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
