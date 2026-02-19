from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'


@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
              filtered_students.append(student) 
        return filtered_students
    return data

@app.get('/stats')
async def get_stats():
    stats = {}
    for student in data:
        pref = student.get('pref')
        programme = student.get('programme')

        if pref:
            stats[pref] = stats.get(pref, 0) + 1
        
        if programme:
            stats[programme] = stats.get(programme, 0) + 1
            
    return stats


@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return {"result": a + b}

@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return {"result": a * b}

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}