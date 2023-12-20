from .components.image.routers import images
from .components.task.services.task_runner import TaskRunner
from .components.user.routers import users
from .components.auth.routers import auth
from .components.trip.routers import flights
from .components.task.routers import tasks
from fastapi import FastAPI
from .db.database import engine, Base
from multiprocessing import Process

Base.metadata.create_all(bind=engine)
app = FastAPI(title="EasyTrip AI")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(images.router)
app.include_router(flights.router)
app.include_router(tasks.router)

task_runner = TaskRunner()
p = Process(target=task_runner.run)
p.daemon = True
p.start()
