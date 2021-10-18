from pathlib import Path
import re
from git import Repo
from include_resolver import resolve_includes
from style_resolver import resolve_styles 
from path_resolver import resolve_paths 

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
        offset = re.search('<div class="w3-content" style="max-width:2000px;margin-top:0px">', content).span()[1]
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
    return resolve_paths(new_content, filepath)

def _resolve_file(content, filepath):

    content = resolve_includes(content, filepath)

    content = resolve_styles(content)

    content = resolve_paths(content, filepath)
    
    return content

def _convertPartialToHtmlPath(path):
    filename = path.name.split('.')[0] + ".html"
    file_result_path = path.parent.joinpath(filename)
    return file_result_path


def _transform_html_file(path):
    with open(path, 'r') as file_object:
        content = file_object.read()

        new_file_content = _resolve_file(content, path)

        # if new_file_content.find("index") > -1: 
        new_file_content = _nav_bar(new_file_content, path)

        new_path = _convertPartialToHtmlPath(path)
        
        with open(new_path, 'w') as new_file_object:
            new_file_object.write(new_file_content)

        print(path.name + " => " + new_path.name)    


  
repo = Repo("..")
assert not repo.bare
git = repo.git
files = git.diff('--name-only', '--cached').split('\n')
untracked_files = repo.untracked_files
files = files + untracked_files


#Get all html files
for file in filter(lambda f: f.endswith('.partial.html'), files):
    root_path="../"
    path=Path(root_path+file)
    if(path.exists()):
        _transform_html_file(Path(path))
      