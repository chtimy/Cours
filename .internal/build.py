from pathlib import Path
import re
from git import Repo

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
        print("Error parsing argument : " + content)
    if(values[1].startswith("{") and values[1].endswith("}")):
        values[1] = values[1][1:len(values[1])-1]
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
        if content[i] == '{' and not openCloseQuote:
            openCloseBrackets += 1
        if content[i] == ')' and openCloseBrackets > 0 and not openCloseQuote:
            openCloseBrackets -= 1
        if content[i] == '}' and not openCloseQuote:
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
    print(args)
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

styles={'%div%' : 'class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px"',
        '%p%'   : 'class="w3-justify w3-large"',
        '%img%' : 'style="max-width:800px; width:100%; height:60%;"',
        '%ul%'  : 'class="w3-large" style="text-align: left;"'}
def _resolve_styles(content):
    for key, value in styles.items():
        content = content.replace(key, value)
    return content

def _nav_bar(content, filepath):
    match = re.finditer('<h2.*>(?P<title>.*)</h2>', content)
    if match:
        i = 0
        nav = '\n<div class="w3-sidebar w3-opacity" style="width: 20%; margin-top:20vh">\n'
        nav = nav + '<a href="%rootpath%/../index.html" class="w3-bar w3-green w3-left-align w3-button w3-mobile">Accueil</a>\n'
        for m in match:
            nav = nav + '<a href="#Part'+str(i)+'" class="w3-bar w3-border-bottom w3-left-align w3-button w3-mobile">'+m.group("title")+'</a>\n'
            i = i + 1
        nav = nav + '</div>\n'
        offset = re.search('<div class="w3-content" style="max-width:2000px;margin-top:46px">', content).span()[1]
        content = content[:offset] + nav + content[offset:]
        i = 0

    match = re.finditer('<h2.*>(?P<title>.*)</h2>', content)
    new_content = ""
    last_offset = 0     
    for m in match:
        new_content = new_content + content[last_offset:m.start("title")-1] + ' id="Part' + str(i) + '"'
        i = i + 1
        last_offset = m.start("title")-1
    new_content = new_content + content[last_offset:]
    return _resolve_paths(new_content, filepath)

def _resolve_file(content, filepath):

    content = _resolve_includes(content, filepath)

    content = _resolve_styles(content)

    content = _resolve_paths(content, filepath)
    
    return content

def _convertPartialToHtmlPath(path):
    filename = path.name.split('.')[0] + ".html"
    file_result_path = path.parent.joinpath(filename)
    return file_result_path


def _transform_html_file(path):
    with open(path, 'r') as file_object:
        content = file_object.read()

        new_file_content = _resolve_file(content, path)

        new_file_content = _nav_bar(new_file_content, path)

        new_path = _convertPartialToHtmlPath(path)
        
        with open(new_path, 'w') as new_file_object:
            new_file_object.write(new_file_content)

        print(path.name + " => " + new_path.name)    


  
repo = Repo("..")
assert not repo.bare
git = repo.git
files = git.diff('--name-only').split('\n')
untracked_files = repo.untracked_files
files = files + untracked_files


#Get all html files
for file in filter(lambda f: f.endswith('.partial.html'), files):
    root_path="../"
    path=Path(root_path+file)
    if(path.exists()):
        _transform_html_file(Path(path))
      