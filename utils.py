def build_file(cmd, val, file):
    if cmd == 'filter':
        res = [x for x in file if val in x]
    elif cmd == 'map':
        res = [i.split(' ')[int(val)] for i in file]
    elif cmd == 'unique':
        res = list(set(file))
    elif cmd == 'sort':
        res = sorted(file, reverse=False if val == 'asc' else True)
    elif cmd == 'limit':
        res = list(file)[:int(val)]

    return res
