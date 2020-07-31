from django.http import HttpResponse


def index(request):
    return HttpResponse('Велком пейдж<br>' + menu_list('/'))


def contacts(request):
    return HttpResponse('Контакты page<br>' + menu_list('/contacts'))


def article(request):
    return HttpResponse('Статьи page<br>' + menu_list('/article'))


def menu_list(current_url):
    items = [
        {'name': 'Велком пейдж', 'url': '/'},
        {'name': 'Контакты', 'url': '/contacts'},
        {'name': 'Статьи', 'url': '/article'},
    ]
    menu = ''
    for item in items:
        style_class = ''
        if current_url != item['url']:
            style_class = 'current'
        menu = menu + create_url(item['url'], item['name'], style_class) + ' '

    return menu


def create_url(href, name, style_class=''):
    return '<a class="' + style_class + '" href="' + href + '">' + name + '</a>'
