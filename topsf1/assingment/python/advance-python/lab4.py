 # Create and write
f = open("demo.txt", "w")
f.write("Hello File")
f.close()

# Read and print
f = open("demo.txt", "r")
print(f.read())
f.close()

# File cursor position
f = open("demo.txt", "r")
print(f.tell())
f.close()