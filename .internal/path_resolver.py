def resolve_paths(data, targetFilePath):
    path = str(targetFilePath.parent)
    deep = len(path.split('\\')) - 1
    newPath = ""
    for x in range(deep):
        newPath += "../"
    internal_path = newPath+".internal"
    data = data.replace("%rootpath%", internal_path)
    java_cours_path = newPath+"java/Cours"
    data = data.replace("%java_cours%", java_cours_path)
    cpp_cours_path = newPath+"cpp/fiches"
    data = data.replace("%cpp_cours%", cpp_cours_path)
    cpp_exercices_path = newPath+"cpp/exercices"
    data = data.replace("%cpp_exercices%", cpp_exercices_path)
    java_projet_path = newPath+"java/Projets"
    data = data.replace("%java_projets%", java_projet_path)

    return data