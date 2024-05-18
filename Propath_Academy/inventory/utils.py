import json
from .models import Item, Kit
def json_to_html_table(json_list):
    data = json.loads(json_list)
    keys = list(data[0].keys())
    if 'item' in keys:
        keys.remove('item')
        keys.insert(0, 'item')
    if 'kit' in keys:
        keys.remove('kit')
        keys.insert(0, 'kit')

    html_table = '<table border="1">\n'
    
    html_table += '<tr>'
    for key in keys:
        if key == 'item':
            html_table += '<th>Item</th>'
        elif key == 'kit':
            html_table += '<th>Kit</th>'
        else:
            html_table += '<th>Quantity</th>'
    html_table += '</tr>\n'
    
    for item in data:
        html_table += '<tr>'
        for key in keys:
            if key == 'item':
                html_table += '<td>' + Item.objects.get(pk=item[key]).name + '</td>'
            elif key == 'kit':
                html_table += '<td>' + Kit.objects.get(pk=item[key]).name + '</td>'
            else:
                html_table += '<td>' + item[key] + '</td>'
        html_table += '</tr>\n'
    
    html_table += '</table>'
    
    return html_table