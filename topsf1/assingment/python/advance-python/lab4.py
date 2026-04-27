f = open("myfile.txt", "r")
data = f.read()
print(data)
f.close()

f = open("myfile.txt", "w")
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
f.close()

f = open("demo.txt", "w")
f.write("Hello File")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()

f = open("demo.txt", "r")
print(f.tell())
f.close()
