class style():
    formats = {
    'HEADER' : '\033[95m',
    'OKBLUE' : '\033[94m',
    'OKCYAN' : '\033[96m',
    'OKGREEN' : '\033[92m',
    'FAIL' : '\033[91m',
    'PASS' : '\033[32m',
    'ENDC' : '\033[0m',

    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m',
    'RED' : '\033[31m',
    'GREEN' : '\033[32m',
    'BLUE' : '\033[34m',
    'RESET' : '\033[0m',
    }

def format(format, message):
    return style.formats[format] + str(message) + style.formats['RESET']