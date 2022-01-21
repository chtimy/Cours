styles={'%div%' : 'class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px"',
        '%p%'   : 'class="w3-justify w3-large"',
        '%img%' : 'style="max-width:800px; width:100%; height:60%;"',
        '%img60%' : 'style="max-width:800px; width:60%;"',
        '%img50%' : 'style="max-width:800px; width:50%;"',
        '%img40%' : 'style="max-width:800px; width:40%;"',
        '%img30%' : 'style="max-width:800px; width:30%;"',
        '%ul%'  : 'class="w3-large" style="text-align: left;"'}
def resolve_styles(content):
    for key, value in styles.items():
        content = content.replace(key, value)
    return content