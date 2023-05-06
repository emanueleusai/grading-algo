# grading-algo
Grading algorithm for PH 105 and PH 125 at UA spring semester 2023

# commands

git clone git@github.com:emanueleusai/grading-algo.git 

cd grading-algo 

python3 -m venv grading-algo-env

source grading-algo-env/bin/activate 

git config --global submodule.recurse true

git submodule add git@github.com:emanueleusai/grading-data.git

pip install -r requirements.txt

python3 grade.py
