# ANSI escapes. 
colours = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

background = {k : f'{v[0:2]}4{v[3:]}' for k, v in colours.items()}

cursor = {
    'up': '\033[1A',
    'down': '\033[1B',
    'right': '\033[1C',
    'left': '\033[1D',
    'home': '\033[1H',
    'end': '\033[1F',
    'save': '\033[s',
    'restore': '\033[u',
    'hide': '\033[?25l',
    'show': '\033[?25h'
}

text = {
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}
