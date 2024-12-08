cow = str(r"""
                    /)  (\
               .-._((,~~.))_.-,
                `=.   99   ,='
                  / ,o~~o. \
                 { { .__. } }
                  ) `~~~\' (
                 /`-._  _\.-\
                /         )  \
              ,-X            X-.
             /   \          /   \
            (     )| |  | |(     )
             \   / | |  | | \   /
              \_(.-( )--( )-.)_/
              /_,\ ) /  \ ( /._\
                  /_,\  /._\   """)

smiley=(r"""
      _.-'''''-._
    .'  _     _  '.
   /   |_|   |_|   \
  |  ,           ,  |
  |  \`.       .`/  |
   \  '.`'""'"`.'  /
    '.  `'---'`  .'
      '-._____.-'  
""")


def bubble(text):
    list1 = list(text)
    newLen = len(list1)
    topandbottom = []
    for x in range(newLen+6):
        topandbottom.append("-")
    topandbottom = ''.join(topandbottom)
    FINAL = ("", topandbottom, "\n | ", text, " |\n", topandbottom)
    return FINAL


line = (r"""
             \
              \
               \ 
                \
                 \ 
                  \
                   \
                    \
        """)