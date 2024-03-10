import argparse
import os
import sys
from src.algo import decompress

import config.cfg as cfg
from src.algo import compress

parser = argparse.ArgumentParser(
    prog="lz78.py",
    description="LZ-78 compressing app",
)
actions = parser.add_argument_group("Actions")
actions.add_argument(
    "-c",
    "--compress",
    dest="comp",
    help="Compresses data",
    action="store_const",
    const=compress,
)
actions.add_argument(
    "-d",
    "--decompress",
    dest="dec",
    help="Decompresses data",
    action="store_const",
    const=decompress,
)
parser.add_argument(
    "data",
    nargs="?",
    help="Input data",
    action="store",
)

parser.add_argument(
    "-i",
    "--input",
    type=open,
    default=None,
    metavar="path",
    help="The input file",
    action="store",
)
parser.add_argument(
    "-o",
    "--output",
    type=argparse.FileType("w"),
    default=sys.stdout,
    metavar="path",
    help="The output file",
    action="store",
)

args: argparse.Namespace = parser.parse_args()


def flag_parse():
    if args.comp is None and args.dec is None:
        raise ValueError("You must specify action!")
    elif (args.comp is None) == (args.dec is None):
        raise ValueError("You must specify only one action!")

    cfg.INPUT_FILE = args.input
    cfg.IS_INPUT_FILE = args.input is not None

    if args.data is None and not cfg.IS_INPUT_FILE:
        raise ValueError("Must be specified either input file or data!")

    cfg.OUTPUT_FILE = args.output

    if args.comp is not None:
        cfg.ACTION = args.comp
    else:
        cfg.ACTION = args.dec
