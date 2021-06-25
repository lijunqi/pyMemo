import urllib

#f = urllib.urlopen("http://oabt004.com/index/index")
#
#fl = f.readline()
#while len(fl) > 0:
#    print(fl)
#    fl = f.readline()

filename = urllib.urlretrieve('http://oabt004.com/index/index',filename='./index.html')

print("Done.")
