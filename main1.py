from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root(name: str = "Alan"):
    return {"message": f"Hello {name}"}


curl \
  -H 'Content-Type: application/json' \
  http://localhost:8000?name=Steve