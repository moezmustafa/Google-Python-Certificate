filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []

for words in enumerate(filenames):
    if words.endswith(".c" or ".hpp" or ".out" ):
        words = words.replace(".c", ".h")
        words = words.replace(".hpp", ".h")
        words = words.replace(".out", ".h")
        print("\n" + words)
        newfilenames.append(words)


print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]