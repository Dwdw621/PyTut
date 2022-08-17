'''
Random tips
    Search up "python 3 math methods" for more goodies!
    String * int = String repeated by int times!!!!!!
    range(x) produces a sequence of num, from 0 to x-1 with x numbers in total
    Keyword argument: Parameter name and "=" to assign a value to that parameter when calling functions w/ parameters, better readability
'''

'''
Unpacking
    tuple/list = (1,2,3)
    x, y, z = tuple/list
    x now has the value of 1, y has 2, ...
'''

'''
Collections
    The ":" signifies start and end in for index operators, works for collections and strings and more
    Uses [] to access the indexes of collections!
    
    Tuples
        IMMUTABLE   ORDERED     USES ()
    List
        MUTABLE     ORDERED     USES []
    Dictionaries
        MUTABLE     UNORDERED   USES {}
        Stores key-value pairs, e.g. 'age' and int age, 'name' str name, etc.
            Assigns value to key using ":"
'''

'''
Classes & Inheritance
    public class Person extends Mammal{
        public String name;
        public int age;
        
        public Person(name, age){
            this.name = name;
            this.age = age;
        }
    }
    
    class Person(Mammal:
        def __init__(this, n, a):
            this.name = n
            this.age = a
'''

'''
Modules & Package
    Modules should contain all the related functions and classes
        import moduleName                       (Dot operator needed to access)
        from moduleName import functionName     (No dot operator to access)  
        import pkgName.moduleName                       (Dot operator needed to access)
        from pkgName.moduleName import functionName     (No dot operator to access)
'''
typed = input("Phone number is: ")
numberDic = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "0": "Zero"}
#numberDic = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
output = ""
for num in typed:
    output += numberDic.get(num, "?") + " "
print(output)