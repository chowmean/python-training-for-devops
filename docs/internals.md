#Python Internals
####Compiler:
Definition: A compiler is a computer program that transforms (translates) source code of a programming language (the source language) into another computer language (the target language). In most cases compilers are used to transform source code into executable program, i.e. they translate code from high-level programming languages into low (or lower) level languages, mostly assembly or machine code.

Ex:<br> 
1. Java<br> 
2. C++<br>
3. C#<br>

#### Interpreter
Definition: An interpreter is a computer program that executes instructions written in a programming language. Translation occurs at the same time as the program is being executed.
<br>It can either


1. execute the source code directly or
2. translate the source code in a first step into a more efficient representation and execute this code

Ex:<br>
1. java script<br>
2. Python
###How Python runs?
 Have you ever thought how the Python code is actually executed by the Python interpreter? What steps are carried out to generate the final output of your Python script? This article answers all these questions in a simplistic manner!
<br>

![Interprer Interpreter](https://i.imgur.com/iQYveIP.png)

####The interpreter
Interpreter is nothing but a software which can run your Python scripts.

Interestingly, it can be implemented in any programming language!

1. CPython is the default interpreter for Python which is written in C programming language.
2. Jython is another popular implementation of python interpreter written using Java programming language.

####Programmer’s view of interpreter
If you have been coding in Python for sometime, you must have heard about the interpreter  at least a few times.<br> 
From a programmer’s perspective, an interpreter is simply a software which executes the source code line by line.

![Interprer Interpreter](https://i.imgur.com/c0PRvvI.png)

<br>For most of the Python programmers, an interpreter is like a black box.<br>

####Python’s view of interpreter
Now, let us scan through the python interpreter and try to understand how it works.

Have a look at the diagram shown below:
![Interprer Interpreter](https://i.imgur.com/PJME67T.png)

I hope you didn’t get amazed to see a compiler inside an interpreter!

From the figure above, it can be inferred that interpreter is made up of two parts:

1. compiler
2. virtual machine<br>
 
What does compiler do?

   Compiler compiles your source code (the statements in your file) into a format known as byte code. Compilation is simply a translation step!<br>

Byte code is a:

1. lower level,
2. platform independent,
3. efficient and
4. intermediate<br>
representation of your source code!

Roughly, each of your source statements is translated into a group of byte code instructions.

The process of compilation in CPython interpreter’s compiler can be divided into 4 main parts:

* **Parse source code into a parse tree:**<br>
  Based on grammar rules of Python programming language, the source code is converted to a parse tree. Every node of the parse tree contains a part of your code.<br>
  
    Consider a simple arithmetic expression:
    <pre>
    14 + 2 * 3 - 6 / 2
    </pre>
    The parse tree for above expression looks like this:
    ![Interprer Interpreter](https://indianpythonista.files.wordpress.com/2018/01/parsetree.png)
    
* **Transform parse tree into an Abstract Syntax Tree:**<br>
   The abstract syntax tree (AST) is a high-level representation of the program structure.
    Each node of the tree denotes a construct occurring in the source code. The syntax is “abstract” in not representing every detail appearing in the real syntax.Consider the AST shown below for the parse tree example discussed above:
    ![Interprer Interpreter](https://indianpythonista.files.wordpress.com/2018/01/ast.png)
* **Transform AST into a Control Flow Graph:**<br>
    A control flow graph is a directed graph that models the flow of a program using basic blocks. Each block contains the bytecode representation of program code inside it.
* **Byte Code generation from CFG:**<br>
    CFGs are usually one step away from final code output. Code is directly generated from the basic blocks by doing a post-order depth-first search on the CFG following the edges.
    
This byte code translation is performed to speed up the execution—byte code can be run much quicker than the original source code statements.

###What does Virtual Machine do?
As soon as source code gets converted to byte code, it is fed into PVM (Python Virtual Machine).<br>
It’s just a big loop that iterates through your byte code instructions, one by one, to carry out their operations. **The PVM is the runtime engine of Python**; it’s always present as part of the Python system, and is the component that truly runs your scripts. Technically, it’s just the last step of what is called the Python interpreter. 

####Lastly, here are a interesting points:

1. PyPy is an implementation of Python which does not use an interpreter! It is implemented using something called just-in-time compiler!
Interestingly, it often runs faster than the standard implementation of Python, CPython.
2. Whenever a Python script is executed, the byte code is generated in memory and simply discarded when program exits.
3. But, if a Python module is imported, a .pyc file for the module is generated which contains its Byte code.
Thus, when the module is imported next time, the byte code from .pyc file is used, hence skipping the compilation step!

###Question:
when we update source code of imported module, how does interpreter picks up that updated code?  