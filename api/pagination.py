from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'limit'
    page_query_param = 'offset'
    max_page_size = 100
    

    def get_paginated_response(self, data):
        return Response({
            'count':len(data),
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
