def _get_next_brackets_position(content, index):
    while content[index] != '(' and index < len(content):
        index+=1

    if index == len(content):
        return -1, -1

    index+=1
    begin = index
    open_close=1
    for x in range(begin, len(content)):
        if content[x] == '(':
            open_close+=1
        if content[x] == ')':
            open_close-=1
        if open_close == 0:
            index = x
            break
    return begin, index

def parse_includes(content):
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


def parse_include(include):
    template_name, arguments = _parse_arguments(include)
    return {'templateName' : template_name, 'templateArgs' : arguments}

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
    template_name = ""
    while i < len(content):
        if content[i] == ',':
            template_name = content[0:i]
            i+=1
            break
        i+=1
    if template_name == "":
        print("Error parsing include arguments")

    open_close_brackets = 0
    open_close_quote = False
    index = i
    args=[]
    while i < len(content):
        if content[i] == '(' and not open_close_quote:
            open_close_brackets += 1
        if content[i] == '{' and not open_close_quote:
            open_close_brackets += 1
        if content[i] == ')' and open_close_brackets > 0 and not open_close_quote:
            open_close_brackets -= 1
        if content[i] == '}' and not open_close_quote:
            open_close_brackets -= 1
        if content[i] == '"' and open_close_brackets == 0:
            open_close_quote = not open_close_brackets
        if content[i] == ',' and open_close_brackets == 0 and not open_close_quote:
            args.append(content[index:i])
            index = i+1
        if i+1 == len(content):
            args.append(content[index:i+1])
        i+=1

    template_args = []
    for arg in args:
        template_args.append(_parse_argument(arg))
    return template_name, template_args