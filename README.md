# shenshan_python

#Prerequisites
1) install python3.8
2) install Visual Studio Code
3) install wsl2
4) configure visual studio with wsl2.0
    - Open visual studio code
    - Install the remote - wsl extension


2) check virtualenv is installed: 
        virtualenv --version

3) install virtualenv
    sudo pip3 install virtualenv

4) create virtualenv
    virtualenv ~/venv/shenshan_python -p python3.8

5) active virtual environment
    source ~/venv/shenshan_python/bin/activate
   
#unit test 
1) install pybuild
    sudo pip3 install pybuilder
   
2) install pytest
    sudo pip3 install pytest
   
3) install pytest coverage
    sudo pip3 install pytest_cov
   
#install required dependencies
1) pip3 install -U -r requirements.txt

#build the package and run unit test:
1) pyb
