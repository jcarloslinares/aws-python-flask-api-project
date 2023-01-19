## Dependencies
- Required Node v14.19.1 or upper
- Required Python 3.9
- Required serverless framework
## Check Versions

NodeJs

```
$>node --version
v14.19.1
```

Python
```
$>python3 --version
Python 3.7.3
```

Serverless
```
$>serverless --version
Running "serverless" from node_modules
Framework Core: 3.25.1 (local) 3.14.0 (global)
Plugin: 6.2.2
SDK: 4.3.2
```

Checking virtualenv installed
```
pip3 list
    Package      Version
    ------------ -------
    distlib      0.3.6
    filelock     3.8.2
    MarkupSafe   2.1.2
    pip          22.2.2
    platformdirs 2.6.0
    setuptools   65.4.1
    virtualenv   20.17.1
    Werkzeug     2.2.2
    wheel        0.37.1
```
If not you can install by
```
pip3 install virtualenv
```
'VIRTUALENV' Docs --> https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

### Create a virtual env
```
$>virtualenv -p python3 env
    created virtual environment CPython3.10.8.final.0-64 in 784ms
    creator CPython3Posix(dest=/Users/jc/projects/repositories/aws-python-flask-api-project/env, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/jc/Library/Application Support/virtualenv)
    added seed packages: pip==22.3.1, setuptools==65.6.3, wheel==0.38.4
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```
Then Activate it
```
$>source env/bin/activate
    (env) JC:aws-python-flask-api-project jc$
```

### Proyect dependencies
```
$>pip3 install flask
```
For keeping the list of dependecies

```
$>pip3 freeze > requeriments.txt
````
OR if you just want to install from existing requeriments file
```
$>pip3 install -r ./requeriments.txt
````

## Run locally from Serverless: 
$>sls wsgi serve


Test from terminal:
```
$> curl -X GET   'http://localhost:5000/hello'   --header 'Accept: */*'
{
  "message": "Hello from path!"
}
``` 

## Possible issues and solutions:

Python Versions issues  
https://opensource.com/article/19/5/python-3-default-mac

Flask module not found on VS Code
https://stackoverflow.com/questions/65786221/import-flask-could-not-be-resolved-from-source-pylance-reportmissingmodulesou