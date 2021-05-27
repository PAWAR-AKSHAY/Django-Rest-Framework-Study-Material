from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # To set number of records per page, default = 5
    page_query_param = 'mypage'  # To set query param to any word, default = page
    page_size_query_param = 'records'  # To allow client set per page records as per their requirements
    max_page_size = 7  # To limit the per page records
    last_page_strings = 'end'  # To set last_page_strings to any word, default = last
