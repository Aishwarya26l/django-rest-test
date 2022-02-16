def get_paginator(paginator, page, size):
    page_data = paginator.page(page)
    return {
        'total_pages': paginator.num_pages,
        'total_num': paginator.count,
        'current_page': page_data.number,
        'current_num': len(page_data.object_list)
    }

def number_thousand_separator_format(num, round_to=0):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = round(num / 1000.0, round_to)
    return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def calculate_elapsed_time(seconds, granularity=2):
    intervals = (
        ('years', 31536000),    # 60 * 60 * 24 * 365
        ('months', 2592000),    # 60 * 60 * 24 * 30
        ('weeks', 604800),      # 60 * 60 * 24 * 7
        ('days', 86400),        # 60 * 60 * 24
        ('hours', 3600),        # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )
    
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))

    return ', '.join(result[:granularity]) + ' ago'

def truncate(string, length):

    return string[:length] + (string[length:] and '...')