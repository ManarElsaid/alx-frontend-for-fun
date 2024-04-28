#!/usr/bin/python3
"""markdown to html """
import sys
import os
import hashlib
import re


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1], file=sys.stderr))
        exit(1)

    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            for line in read:
                length = len(line)
                headings = line.strip("#")
                heading_count = length - len(headings)
                if 1 <= heading_count <= 6:
                    line = '<h{}>'.format(
                        heading_count) + headings.strip() + '</h{}>\n'.format(
                        heading_count)
                if length > 1:
                    html.write(line)


    exit(0)
