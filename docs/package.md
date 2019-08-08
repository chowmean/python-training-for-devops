# Creating a python package. 

For creating a python file you need below steps. 

### Application Structure
Lets say our app structure is like below

<pre>

firstapp
	--pack.py
	--__init__.py
setup.py
README.md
</pre>

Lets say pack.py contains below code

<pre>
def say_hello():
	print("hello")
</pre>

### Setup file

You need to create a setup.py file which will contain information about the package. 


<pre>
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='firstapp',  
     version='0.1',
     scripts=['firstapp/pack.py'] ,
     author="chowmean",
     author_email="gaurav.dev.iiitm@gmail.com",
     description="Test package creation package",
     long_description="long_description",
     long_description_content_type="text/markdown",
     url="https://gitlab.com/chowmean",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
</pre>

### Other files
init file will be empty and README.md you can put about the project. 

After this you need to make sure setuptools is installed on you environment. Then run this below command. 

### Build package
<pre>
python setup.py bdist_wheel
</pre>

This will create your python package and your package will be present in /dist directory.

To install this package you can simply use the below command. 


### Install local package
<pre>
python -m pip install firstapp-0.1-py2-none-any.whl
</pre>

This will install firstapp in your python environment. You can use it like below. 


### Using Installed package. 
<pre>
from firstapp import pack
pack.say_hello()
</pre>


This will print the Hello from the package. 

This was very basic of how you can create a python pakcage. The advanced thing that you can try is installing all the dependent packages of your application at the time of application installation. 

