from fastapi import FastAPI
from users.router import router as users_router
from order.router import router as order_router
from users.schemas import Settings
from fastapi_jwt_auth import AuthJWT


app = FastAPI()
app.include_router(router=users_router)
app.include_router(router=order_router)


@AuthJWT.load_config
def get_config():
    return Settings()


@app.get('/')
def test():
    return {'message': True}