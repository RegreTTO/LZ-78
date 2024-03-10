#!/bin/env python
import sys
from src.algo import decompress, compress
import config.cfg as cfg
from src.flag_parse import flag_parse
from src.flag_parse import args


def read_data() -> str:
    data: str = None
    if cfg.IS_INPUT_FILE:
        data: str = cfg.INPUT_FILE.read().strip()
        cfg.INPUT_FILE.close()
    else:
        data = args.data
    return data


def main():
    flag_parse()
    data = read_data()
    ret_data = None
    if cfg.ACTION == compress:
        ret_data: list = cfg.ACTION(data)
        if cfg.OUTPUT_FILE == sys.stdout:
            cfg.OUTPUT_FILE.write("Compressed data: ")
    elif cfg.ACTION == decompress:
        ret_data: str = cfg.ACTION(data)
        if cfg.OUTPUT_FILE == sys.stdout:
            cfg.OUTPUT_FILE.write("Decompressed data: ")
    cfg.OUTPUT_FILE.write(str(ret_data))

    if cfg.INPUT_FILE is not None:
        cfg.INPUT_FILE.close()
    cfg.OUTPUT_FILE.close()


if __name__ == "__main__":
    main()
