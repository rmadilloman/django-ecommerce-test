from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5       # Number of products per page
    page_size_query_param = 'page_size'
    max_page_size = 10     # Maximum allowed page size
    page_query_param = 'page'