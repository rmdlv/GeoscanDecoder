import pathlib


__version__ = '0.1.12'

HOMEDIR = pathlib.Path('~/GeoscanDecoder').expanduser().absolute()
CONFIG = HOMEDIR / 'config.ini'
AGWPE_CON = b'\x00\x00\x00\x00k\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
