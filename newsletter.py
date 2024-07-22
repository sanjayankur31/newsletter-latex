#!/usr/bin/env python3
"""
Script to generate a LaTeX newsletter.

File: newsletter.py

Copyright 2024 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import textwrap



def main():
    """Main runner method
    :returns: TODO

    """
    file_contents = ""
    # end of LaTeX file, to be appended at the end to close the document
    file_start = "\\begin{document}\n"
    file_end = "\\end{document}\n"

    # open up the file
    with open("templates/main.tex", 'r') as f:
        file_contents += f.read()
    file_contents += file_start

    # newsletter text
    with open("templates/title.tex", 'r') as f:
        file_contents += f.read()


    file_contents += file_end

    with open("newsletter.tex", 'w') as f:
        print(file_contents, file=f)


if __name__ == "__main__":
    main()
