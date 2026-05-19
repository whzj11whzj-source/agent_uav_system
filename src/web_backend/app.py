
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Command(BaseModel):
    text: str

@app.post('/command')
def command(cmd: Command):

    return {
        'status': 'ok',
        'command': cmd.text
    }
