#!/usr/bin/env python

"""
A script to generate a file named index.html from sheet.md and templace.html
"""

from bs4 import BeautifulSoup
import markdown
import subprocess


top = """
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8">
    <title>Scientific python cheat sheet by IPGP</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.5">
    <link rel="stylesheet" type="text/css" href="stylesheets/normalize.css" media="screen">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen">
    <link rel="stylesheet" type="text/css" href="stylesheets/github-light.css" media="screen">
      <style type="text/css">code{white-space: pre;}</style>
  <style type="text/css">
div.sourceCode { overflow-x: auto; }
table.sourceCode, tr.sourceCode, td.lineNumbers, td.sourceCode {
  margin: 0; padding: 0; vertical-align: baseline; border: none; }
table.sourceCode { width: 100%; line-height: 100%; }
td.lineNumbers { text-align: right; padding-right: 4px; padding-left: 4px; background-color: #dddddd; }
td.sourceCode { padding-left: 5px; }
code > span.kw { color: #a71d5d } /* Keyword */
code > span.dt { color: #800000; } /* DataType */
code > span.dv { color: #009999; } /* DecVal */
code > span.bn { color: #009999; } /* BaseN */
code > span.fl { color: #009999; } /* Float */
code > span.ch { color: #009999 ; } /* Char */
code > span.st { color: #d01040; } /* String */
code > span.co { color: #969896 } /* Comment */
code > span.al { color: #00ff00; font-weight: bold; } /* Alert */
code > span.fu { color: #000080; } /* Function */
code > span.er { color: #ff0000; font-weight: bold; } /* Error */
code > span.wa { color: #ff0000; font-weight: bold; } /* Warning */
code > span.cn { color: #0086b3; } /* Constant */
code > span.sc { color: #ff00ff; } /* SpecialChar */
code > span.vs { color: #dd0000; } /* VerbatimString */
code > span.ss { color: #dd0000; } /* SpecialString */
code > span.im {color: #000080; } /* Import */
code > span.va {color: #000080; } /* Variable */
code > span.cf {color: #000080; } /* ControlFlow */
code > span.op {color: #000080; } /* Operator */
code > span.bu {color: #0086B3; } /* BuiltIn */
code > span.ex { } /* Extension */
code > span.pp { font-weight: bold; } /* Preprocessor */
code > span.at { } /* Attribute */
code > span.do { color: #808080; font-style: italic; } /* Documentation */
code > span.an { color: #808080; font-weight: bold; font-style: italic; } /* Annotation */
code > span.cv { color: #808080; font-weight: bold; font-style: italic; } /* CommentVar */
code > span.in { color: #808080; font-weight: bold; font-style: italic; } /* Information */
  </style>
  </head>
  <body>
    <section class="main-content">
"""


bottom = """
      <footer class="site-footer">
        <span class="site-footer-owner"><a href="https://github.com/IPGP/scientific_python_cheat_sheet">Scientific python cheat sheet</a> is maintained by <a href="https://github.com/IPGP">IPGP</a>.</span>

        <span class="site-footer-credits">This page was generated by <a href="https://pages.github.com">GitHub Pages</a> using the <a href="https://github.com/jasonlong/cayman-theme">Cayman theme</a> by <a href="https://twitter.com/jasonlong">Jason Long</a>.</span>
      </footer>

    </section>
  </body>
</html>
"""

input_file = "sheet.md"
output_file = "sheet.html"

try:
    cmd = "pandoc {} -s -o {}".format(input_file,
                                      output_file)
    print cmd
    subprocess.call(cmd, shell=True)
    soup_sheet = BeautifulSoup(open(output_file), "html.parser")
    list_html = map(str, list(soup_sheet.body.children))
    sheet_html = ''.join(list_html)
    print "went the pandoc way"
except:
    print "pandoc failed, using shitty markdown"
    with open(input_file, "r") as f:
        text = f.read()
    sheet_html = markdown.markdown(text)

sheet_html_lines = sheet_html.split("\n")
f = open("index.html", "w")
flag_first_h2 = False
f.write(top+"\n")
for line in sheet_html_lines:
    if "markdown-toc" in line:
        continue

    if "h2" in line:
        if flag_first_h2:
            f.write('</div>\n<div class="group">\n')
            f.write(line+"\n")
        else:
            f.write('<div class="group">\n')
            f.write(line+"\n")
            flag_first_h2 = True
    else:
        f.write(line+"\n")

f.write("</div>\n")
f.write(bottom+"\n")
f.close()
