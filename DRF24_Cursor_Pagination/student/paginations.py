from rest_framework.pagination import CursorPagination


# Mostly used in blog
class CustomPagination(CursorPagination):
    page_size = 5  # Number of records per page
    ordering = 'name'  # Order by any field,If created field is already in the model then it will automatically order by
    cursor_query_param = 'cu'  # To set cursor_query_param any word, by default = cursor
