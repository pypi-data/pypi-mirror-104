import re


class OwofyData:
    owofy_letters = {'r': 'w',
                     'l': 'w',
                     'R': 'W',
                     'L': 'W',
                     'na': 'nya',  # please stop.
                     'ne': 'nye',
                     'ni': 'nyi',
                     ' no ': ' nu ',
                     ' nO ': ' nU ',
                     ' NO ': ' NU ',
                     ' No ': ' Nu ',
                     'no': 'nyo',
                     'nu': 'nyu',
                     'Na': 'Nya',  # oh no the capitalization
                     'Ne': 'Nye',
                     'Ni': 'Nyi',
                     'No': 'Nyo',
                     'Nu': 'Nyu',
                     'nA': 'nyA',  # aaaaaaaaaaaaaaaaaaaaaaaaaa
                     'nE': 'nyE',
                     'nI': 'nyI',
                     'nO': 'nyO',
                     'nU': 'nyU',
                     'NA': 'NYA',  # this is mental torture.
                     'NE': 'NYE',
                     'NI': 'NYI',
                     'NO': 'NYO',
                     'NU': 'NYU',  # I f***ing hate myself.
                     'the ': 'de ',
                     'THE ': 'DE ',
                     'THe ': 'De ',
                     'The ': 'De ',
                     'tHE ': 'dE ',
                     'thE ': 'dE ',  # you seem to have found the exact place where i lose motivation
                     'tt': 'dd',
                     'ock': 'awk',
                     'uck': 'ek',
                     'ou': 'u',
                     'tT': 'dD',
                     'Tt': 'Dd',
                     'TT': 'DD',
                     'ocK': 'awK',
                     'oCK': 'aWK',
                     'OCK': 'AWK',
                     'OCk': 'AWk',
                     'Ock': 'Awk',
                     'ucK': 'eK',
                     'uCK': 'eK',
                     'UCK': 'EK',
                     'UCk': 'Ek',
                     'Uck': 'Ek',
                     'oU': 'U',
                     'OU': 'U',
                     'Ou': 'u'}  # removed stuff because... well, some didn't even work right.
    # holy shit phos, thanks. really. i still had to do all of the caps and stuff but wow.
    owofy_exclamations = [' OwO', ' @w@', ' #w#', ' UwU', ' ewe', ' -w-', ' \'w\'', ' ^w^', ' >w<', ' ~w~', ' ¬w¬',
                          ' o((>ω< ))o', ' (p≧w≦q)', ' ( •̀ ω •́ )y', ' ✪ ω ✪', ' (。・ω・。)', ' (^・ω・^ )']
    # Why'd I put so many here?


to_replace = {
    '<b>': '**',
    '</b>': '**',
    '<p>': '\n**',
    '</p>': '**\n',
    '</li>': '\n'
}

protondb_colors = {"Platinum": 0xB7C9DE, "Gold": 0xCFB526, "Silver": 0xC1C1C1, "Bronze": 0xCB7F22, "Borked": 0xF90000}


def format_html(str_input: str):
    for old, new in to_replace.items():
        str_input = str_input.replace(old, new)
    p = re.compile(r'<.*?>')
    return p.sub('', str_input)


def format_names(name_list: list):
    name_count = len(name_list) - 1
    names = ""
    for idx, name in enumerate(name_list):
        if idx == 0:
            # First name
            names = name
        elif idx == name_count:
            # Last name
            names = names + " and " + name
        else:
            # A name.
            names = names + ", " + name
    return names
