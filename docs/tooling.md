To begin with python tooling, lets first see what these tools are used for. 
# Starting a project
To start any project it is always recommended to create the project in its own environment. This means that anything that is installed for python at global level will not affect this env anf vice versa. 

## How to start development?

### VirutalENV:

Install virtualenv

	sudo apt-get install virtualenv

After installation activate it. 

	virtualenv env_name -m python3

This will create an env for python 3 and you can start working inside it. Keep in mind that you have to activate the env before running your code to make it work. 

Activate env:

	sourve env_name/bin/activate

Now you can install any packages that you want to use in your python program. 

Deactivate env: 

	deactivate

### Pep8 formatting. 

Pep8 is the formatting style that defines how you should format your python program. How you should name your variables and more such conventions. 
Pep8 is highly recommende for anyone who want to work with opensource community. 

### Dependency Management

For dependency management in python we use pip. It is used for installing packages. You can have a file naming requirements.txt which will have all the packages that you need to install along with the version that you want to install. 

##### How to install python package: 

	pip install package_name

##### How to install using requirements.txt

	pip install -r requirements.txt

### Editor?

Pycharm is very good for python but if you are power user of sublime that will be awesome. 