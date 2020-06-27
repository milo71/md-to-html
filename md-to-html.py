import sys
import markdown
import getopt

inputfile = sys.argv[1:]
outputfile = sys.argv[2:]
opts, args = getopt.getopt(inputfile,'i')
opts, args = getopt.getopt(outputfile,'i')

inputfile = open(inputfile[1],'r')
outputfile = open(outputfile[2],'w')

htmlhead = '<html>\n<head>\n</head>\n<body>'
htmlfoot = '\n</body>\n</html>'
html = markdown.markdown(inputfile.read())
htmldoc = htmlhead+html+htmlfoot

outputfile.write(htmldoc)
