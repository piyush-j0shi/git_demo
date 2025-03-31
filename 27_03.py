from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home_page():
    return null

@app.get('/{name}')
def print_name(name):
    return f'hello {name}'
