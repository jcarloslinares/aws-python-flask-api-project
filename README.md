python --version
    Python 3.7.3

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

VIRTUALENV DOC --> https://sourabhbajaj.com/mac-setup/Python/virtualenv.html

virtualenv -p python3 env
    created virtual environment CPython3.10.8.final.0-64 in 784ms
    creator CPython3Posix(dest=/Users/jc/projects/repositories/aws-python-flask-api-project/env, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/jc/Library/Application Support/virtualenv)
    added seed packages: pip==22.3.1, setuptools==65.6.3, wheel==0.38.4
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator


source env/bin/activate
    (env) JC:aws-python-flask-api-project jc$

pip install flask

pip freeze > requeriments.txt

pip install -r ./requeriments.txt

SERVERLESS

RUN LOCALLY: 
sls wsgi serve


TEST: 
http://localhost:5000
