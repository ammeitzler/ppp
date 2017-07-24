greet = "yo"
r = random(1, 10)

str = open('/Users/angelinemeitzler/Documents/Code/sfpc/ppp/testdata.txt')
lines = str.read().split(',')

random_line = lines[r]

print (random_line)

results = list()
for linez in str.readlines():
    #print linez
    results.append(linez)


fill(0.2)
font("Helvetica", 35)
text(greet, 50, 900)
#test_txt = open("/Users/angelinemeitzler/Documents/Code/sfpc/ppp/testdata.txt").read()
#print test_txt

fill(0.2)
x = 200 
y = 40
rect(x,y,100,150)