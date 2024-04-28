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
            unordered_list_start = False
            for line in read:
                length = len(line)
                headings = line.strip("#")
                heading_count = length - len(headings)
                unordered_list = line.strip("-")
                unordered_count = length - len(unordered_list)

                if 1 <= heading_count <= 6:
                    line = '<h{}>'.format(
                        heading_count) + headings.strip() + '</h{}>\n'.format(
                        heading_count)
                if unordered_count:
                    if not unordered_list_start:
                        html.write('<ul>\n')
                        unordered_list_start = True
                    line = '<li>' + unordered_list.strip() + '</li>\n'
                if unordered_list_start and not unordered_count:
                    html.write('</ul>\n')
                    unordered_list_start = False

                if length > 1:
                    html.write(line)
    exit(0)
