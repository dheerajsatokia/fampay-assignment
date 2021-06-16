from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page_size"

    def paginate_queryset(self, queryset, request, view=None):
        if "all" in request.query_params:
            page_size = queryset.count() or self.page_size
            paginator = self.django_paginator_class(queryset, page_size)
            page_number = request.query_params.get(self.page_query_param, 1)
            self.page = paginator.page(page_number)
            self.request = request
            return list(self.page)
        return super().paginate_queryset(queryset, request, view)
