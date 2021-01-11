from flask import Flask, request
import redis
from rq import Queue
import time, os
from modules.background import background_task

os.system('rq worker &')
app =  Flask(__name__)
r = redis.Redis()
q = Queue(connection = r)



@app.route('/')
def hello():
    return 'hello'


@app.route('/task')
def add_task():
    if request.args.get('n'):
        # try:
        var = request.args.get('n')
        print('var: ', var)
        job = q.enqueue(background_task, var)
        q_len = len(q)
        return f'task {job.id} added to queat at {job.enqueued_at}. {q_len} tasks in queue'
        # except Exception as e:
        #     return str(e)

    return 'No value for n'

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
