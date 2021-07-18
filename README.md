create env

```bash 
conda create -n wineq python=3.8 -y
```

activate env
```bash
conda activate wineq

```

created requirements.txt 

install the requirements
```bash
pip install -r requirements.txt

```

git init

dvc init

dvc add data_given/winequality.csv

git add . 

git commit -m "first commit"

git remote add origin https://github.com/rickspark4/dvc-demo.git

git branch -M main

git push origin main

one liner update 
```bash
git add . && git commit -m "msg"
```
```bash
dvc repro
```
dvc metrics show

dvc metrics diff




