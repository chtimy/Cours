from include_parser import parse_includes, parse_include
from style_resolver import resolve_styles 
from path_resolver import resolve_paths 


def _resolve_file(content, filepath):

    content = resolve_includes(content, filepath)

    content = resolve_styles(content)

    content = resolve_paths(content, filepath)
    
    return content

def _resolve_arguments(content, arguments):
    for argument in arguments:
        name = argument['name']
        value = argument['value']
        content = content.replace("%"+name+"%", value)
    return content

def apply_place_holders(content, place_holders):
    new_content = ""
    cursor = 0
    for place_holder in place_holders:
        new_content += content[cursor:place_holder['begin']] + place_holder['content']
        cursor = place_holder['end']
    new_content+=content[cursor:len(content)]
    return new_content

def _load_template(templateName, arguments, targetFilePath):
    templatePath = "./templates/"+templateName+".html.template"
    with open(templatePath, 'r') as file_object:
        filedata = file_object.read()
        filedata = _resolve_arguments(filedata, arguments) 
        filedata = _resolve_file(filedata, targetFilePath)
        return filedata

def resolve_includes(content, filePath):     
    include_occurences = parse_includes(content)
    place_holders = []

    for include_occurence in include_occurences:
        include_arguments = parse_include(include_occurence['content'])
        template = _load_template(include_arguments['templateName'], include_arguments['templateArgs'], filePath)
        place_holders.append({
            'begin' : include_occurence['begin'],
            'end' : include_occurence['end'],
            'content' : template
        })

    return apply_place_holders(content, place_holders)