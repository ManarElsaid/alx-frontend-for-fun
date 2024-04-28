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
            unordered_list_start, ordered_list_start, paragraph = False, False, False
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                length = len(line)
                headings = line.lstrip("#")
                heading_count = length - len(headings)
                unordered_list = line.lstrip("-")
                unordered_count = length - len(unordered_list)
                ordered_list = line.lstrip("*")
                ordered_count = length - len(ordered_list)

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

                if ordered_count:
                    if not ordered_list_start:
                        html.write('<ol>\n')
                        ordered_list_start = True
                    line = '<li>' + ordered_list.strip() + '</li>\n'
                if ordered_list_start and not ordered_count:
                    html.write('</ol>\n')
                    ordered_list_start = False

                if not (heading_count or unordered_list_start or
                        ordered_list_start):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html.write(line)

            if unordered_list_start:
                html.write('</ul>\n')
            if ordered_list_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit(0)
