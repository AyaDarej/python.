# text_file="What is Python language? Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.The best way we learn anything is by practice and exercise questions. We  have started this section for those (beginner to intermediate) who are familiar with Python"
# print(text_file)
myfile_read = open('myfile.txt','r')
#myfile_write = open('myfile.txt','w')
#myfile_append = open('myfile.txt','a')
#myfile_write_or_create = open('myfile.txt','w+')
rows = myfile_read.readlines()
print(rows)
myfile_read.close()

with open("myfile.txt", "r") as fp:
    content = fp.read()
    print(content)
myfile_read.close()
