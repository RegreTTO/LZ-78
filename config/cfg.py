import os
import sys

ROOT_DIR = os.path.abspath(os.curdir)
INPUT_FILE = sys.stdin
OUTPUT_FILE = sys.stdout


IS_INPUT_FILE = False
ACTION: callable = None

