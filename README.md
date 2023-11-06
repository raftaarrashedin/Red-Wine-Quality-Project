creat env

```bash
conda create -n wine_quality python=3.0 - y
```

activate env

```bash
conda activate wine_quality
```
created a requirements.txt file

install the requirements 

```bash
pip install -r requirements.txt 
```
``` bash
git init
```

``` bash
dvc init
```

```bash
dvc add data_given/winequality-red.csv
```

```bash
git add .
```

```bash
git commit -m "first commit in this project"
```


onliner updates for readme file
```bash
git add . && git commit -m "update readme.md"

git remote add origin https://github.com/raftaarrashedin/Red-Wine-Quality-Project.git

git branch -M main

git push -u origin main
```

second day
``` bash
type nul > src/get_data.py
pip install pandas
python src/get_data.py
doskey/history
```

Completed stage 1
``` bash
dvc repro
git add . && git commit -m "stage 1 completed"
git push origin main
```

Splitted the dataset

Tracker Added

Pytest and tox installed

tox command
```bash
tox
```
for rebuilding
```bash
tox -r
```
pytest command 
```bash
pytest -v
```
setup commands 
```bash
pip install -e .
```
Setup done
```bash
python setup.py sdist bdist_wheel
tox
```