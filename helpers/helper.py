from django.core.paginator import Paginator


class Helper:
    def get_with_pagination(self, dataORM, page_number, page_size):
        paginator = Paginator(dataORM, page_size)
        page_objs = paginator.get_page(page_number)

        return {
            'paginator':
                {
                    "page_size": page_size,
                    "current_page": page_number,
                    "max_num_pages": paginator.num_pages,
                    "has_next": page_objs.has_next(),
                    "data_count": dataORM.count(),
                    "has_previous": page_objs.has_previous(),
                },
            'data': page_objs
        }
