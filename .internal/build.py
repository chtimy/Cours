from pathlib import Path
import re

def _get_next_brackets_position(content, index):
    while content[index] != '(' and index < len(content):
        index+=1

    if index == len(content):
        return -1, -1

    index+=1
    begin = index
    openClose=1
    for x in range(begin, len(content)):
        if content[x] == '(':
            openClose+=1
        if content[x] == ')':
            openClose-=1
        if openClose == 0:
            index = x
            break
    return begin, index

def _parse_includes(content):
    index = 0
    includes = []
    while index < len(content):
        local_index = content[index:].find("_include")
        if local_index >= 0 :
            begin, end = _get_next_brackets_position(content, index+local_index)
            if begin+1==end:
                print("Error, brackets are empty")
            includes.append({'begin':index+local_index, 'end':end+1, 'content':content[begin:end]})
            index = end+1
        else:
            break
    return includes

def _resolve_paths(data, targetFilePath):
    path = str(targetFilePath.parent)
    deep = len(path.split('\\')) - 1
    newPath = ""
    for x in range(deep):
        newPath += "../"
    internalPath = newPath+".internal"
    data = data.replace("%rootpath%", internalPath)
    javaCoursPath = newPath+"java/Cours"
    data = data.replace("%java_cours%", javaCoursPath)
    return data

def _resolve_arguments(content, arguments):
    for argument in arguments:
        name = argument['name']
        value = argument['value']
        content = content.replace("%"+name+"%", value)
    return content

def _load_template(templateName, arguments, targetFilePath):
    templatePath = "./templates/"+templateName+".html.template"
    with open(templatePath, 'r') as file_object:
        filedata = file_object.read()
        filedata = _resolve_arguments(filedata, arguments) 
        filedata = _resolve_file(filedata, targetFilePath)
        return filedata

def _parse_argument(content):
    values = content.split('=', 1)
    if len(values) != 2:
        print("Error parsing argument")
    return {'name':values[0], 'value':values[1]}

def _parse_arguments(content):
    i = 0
    index = -1
    templateName = ""
    while i < len(content):
        if content[i] == ',':
            templateName = content[0:i]
            i+=1
            break
        i+=1
    if templateName == "":
        print("Error parsing include arguments")

    openCloseBrackets = 0
    openCloseQuote = False
    index = i
    args=[]
    while i < len(content):
        if content[i] == '(' and not openCloseQuote:
            openCloseBrackets += 1
        if content[i] == ')' and openCloseBrackets > 0 and not openCloseQuote:
            openCloseBrackets -= 1
        if content[i] == '"' and openCloseBrackets == 0:
            openCloseQuote = not openCloseBrackets
        if content[i] == ',' and openCloseBrackets == 0 and not openCloseQuote:
            args.append(content[index:i])
            index = i+1
        if i+1 == len(content):
            args.append(content[index:i+1])
        i+=1

    templateArgs = []
    for arg in args:
        templateArgs.append(_parse_argument(arg))
    return templateName, templateArgs
        
def _parse_include(include):
    template_name, arguments = _parse_arguments(include)
    return {'templateName' : template_name, 'templateArgs' : arguments}

def applyPlaceHolders(content, placeHolders):
    newContent = ""
    cursor = 0
    for placeHolder in placeHolders:
        newContent+=content[cursor:placeHolder['begin']] + placeHolder['content']
        cursor = placeHolder['end']
    newContent+=content[cursor:len(content)]
    return newContent

def _resolve_includes(content, filePath):     
    includeOccurences = _parse_includes(content)
    placeHolders = []

    for includeOccurence in includeOccurences:
        includeArguments = _parse_include(includeOccurence['content'])
        template = _load_template(includeArguments['templateName'], includeArguments['templateArgs'], filePath)
        placeHolders.append({
            'begin' : includeOccurence['begin'],
            'end' : includeOccurence['end'],
            'content' : template
        })

    return applyPlaceHolders(content, placeHolders)

def _resolve_styles(content):
    content = content.replace('%div%', 'class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px"')
    content = content.replace('%p%', 'class="w3-justify w3-large"')
    return content


def _resolve_file(content, filepath):

    content = _resolve_includes(content, filepath)

    content = _resolve_styles(content)

    content = _resolve_paths(content, filepath)
    
    return content

def _convertPartialToHtmlPath(path):
    filename = path.name.split('.')[0] + ".html"
    fileResultPath = path.parent.joinpath(filename)
    return fileResultPath


def _transform_html_file(path):
    with open(path, 'r') as file_object:
        content = file_object.read()
        newFileContent = _resolve_file(content, path)

        newPath = _convertPartialToHtmlPath(path)
        
        with open(newPath, 'w') as new_file_object:
            new_file_object.write(newFileContent)

        print(path.name + " => " + newPath.name)    


#Get all html files
for path in Path('..').rglob('projet.partial.html'):
    _transform_html_file(path)
    