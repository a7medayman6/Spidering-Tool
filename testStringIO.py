import io


s = "dasasdas\nasdasdas\nasdasdadas\nasdsadas\n"
ss = io.StringIO(s)
#print (ss.read())

index = 0
for line in ss:
    index += 1
    if 's' in line:
        print (index)