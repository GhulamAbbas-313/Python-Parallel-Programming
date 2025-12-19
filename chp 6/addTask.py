

###
### addTask.py :Executing a simple task
###

from **celery** import **celery**
#app = Celery('addTask', broker='redis://localhost:6379/0')

app = Celery('addTask', broker='amap://guest@localhost/')

@app.task
def add(x, y):
    return x + y