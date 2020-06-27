import sys
import markdown
import argparse

ap = argparse.ArgumentParser(description='Parse markdown to html')
ap.add_argument('-i', '--input', required=True, help='input file name')
ap.add_argument('-o', '--output', required=True, help='output file name')

args = ap.parse_args()

with open(args.input,'r') as inputfile:
    htmlhead = '<html>\n<head>\n</head>\n<body>'
    htmlfoot = '\n</body>\n</html>'
    html = markdown.markdown(inputfile.read())
    htmldoc = htmlhead+html+htmlfoot

with open(args.output,'w') as outputfile:
    outputfile.write(htmldoc)
