"""latex equation magic, powered by https://www.codecogs.com/"""
__version__ = '0.0.1'
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from IPython.display import Image
import urllib.parse

@magics_class
class LaTeXEqnMagics(Magics):
    def __init__(self, shell):
        super(LaTeXEqnMagics, self).__init__(shell)

    @magic_arguments()
    @argument(
        '-f', '--format', action='store', type=str, default='gif',
        help='output format: gif, png, pdf, swf, emf, svg'
        )
    @argument(
        '-s', '--size', action='store', type=str, default='normal',
        help='equation font size: tiny, small, normal, large, LARGE, huge'
        )
    @argument(
        '-r', '--resolution', action='store', type=str, default="110",
        help='output resolution'
        )
    @argument(
        '-b', '--background', action='store', type=str, default='transparent',
        help='background color: transparent, white, black, red, green, blue'
        )
    @argument(
        '-i', '--inline', action='store', type=bool, default=False,
        help='inline mode'
        )
    @cell_magic
    def latexeqn(self, line, cell):
        args = parse_argstring(self.latexeqn, line)
        typ = args.format
        size = '\\%s&space;'%urllib.parse.quote(args.size) if args.size != 'normal' else ''
        dpi = '\\dpi{%s}&space;'%urllib.parse.quote(args.resolution) if args.resolution != 110 else ''
        bg = '\\bg_%s&space;'%urllib.parse.quote(args.background) if args.background != 'transparent' else ''
        md = '\\inline&space;' if args.inline else ''
        code = urllib.parse.quote(cell)
        templete = "https://latex.codecogs.com/{typ}.latex?{size}{dpi}{bg}{md}{code}"
        url = templete.format(typ=typ, size=size, dpi=dpi, bg=bg, md=md, code=code)
        return Image(url=url)

def load_ipython_extension(ipython):
    ipython.register_magics(LaTeXEqnMagics)
