"""lit-junkie logo"""

LOGO = """
         ,..........   ..........,
     ,..,'          '.'          ',..,
    ,' ,'            :            ', ',
   ,' ,'             :             ', ',
  ,' ,'              :              ', ',
 ,' ,'............., : ,.............', ',
,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';''''''''''''''''''
                    '''
    █░░ █ ▀█▀ ▄▄ ░░█ █░█ █▄░█ █▄▀ █ █▀▀
    █▄▄ █ ░█░ ░░ █▄█ █▄█ █░▀█ █░█ █ ██▄
"""


def get_logo_width():
    """Gets the logos width."""
    width = 0
    for row in LOGO.split("\n"):
        if len(row) > width:
            width = len(row)
    return width


LOGO_WIDTH = get_logo_width()
