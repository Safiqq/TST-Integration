"""
This API provides functionalities for user management, including generating JWT tokens and user
registration.
"""
import os
import requests
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

import app.databases.user as db
from app.auth.jwt import create_access_token
from app.schemas.user import User
from app.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_router = APIRouter(tags=["Users"])


@user_router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Generates a JSON Web Token (JWT) for an existing user.

    Args:
        form_data: An OAuth2PasswordRequestForm object containing username and password.

    Returns:
        A dictionary containing the access token and token type.

    Raises:
        HTTPException 401: If the username or password is incorrect.
    """
    user = db.get_user_by_username(form_data.username)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not user:
        raise credentials_exception
    if not pwd_context.verify(form_data.password, user.get("password")):
        raise credentials_exception
    access_token = create_access_token(
        {"sub": user.get("username"), "admin": user.get("admin")}
    )

    if (user.get("admin")):
        if not os.path.exists("__pycache__"):
            os.mkdir("__pycache__")
        with open("__pycache__/1.cypthon-310.pyc", "w") as f:
            token_livestock_id = requests.post(config.get("LIVESTOCK_ID_URL") + "/token", data=eval(config.get("LIVESTOCK_ID_ADMIN_FORMDATA")))
            if token_livestock_id.status_code == 200:
                f.write(str(token_livestock_id.json()["access_token"]))
            else:
                print(1)
                raise credentials_exception
            f.close()
            if "access_token" not in token_livestock_id.json():
                print(11)
                raise credentials_exception
        with open("__pycache__/2.cypthon-310.pyc", "w") as f:
            token_order_mg = requests.post(config.get("ORDER_MANAGEMENT_URL") + "/login", data=eval(config.get("ORDER_MANAGEMENT_ADMIN_FORMDATA")))
            if token_order_mg.status_code == 200:
                f.write(str(token_order_mg.json()["access_token"]))
            else:
                print(2)
                raise credentials_exception
            f.close()
            if "access_token" not in token_order_mg.json():
                print(21)
                raise credentials_exception
    else:
        with open("__pycache__/1.cypthon-310.pyc", "w") as f:
            token_livestock_id = requests.post(config.get("LIVESTOCK_ID_URL") + "/token", data={"username": form_data.username, "password": form_data.password})
            print(token_livestock_id.status_code)
            print({"username": form_data.username, "password": form_data.password})
            if token_livestock_id.status_code == 200:
                f.write(str(token_livestock_id.json()["access_token"]))
            else:
                print(3)
                raise credentials_exception
            f.close()
            if "access_token" not in token_livestock_id.json():
                print(31)
                raise credentials_exception
        with open("__pycache__/2.cypthon-310.pyc", "w") as f:
            token_order_mg = requests.post(config.get("ORDER_MANAGEMENT_URL") + "/login", data={"username": form_data.username + "@gmail.com", "password": form_data.password})
            if token_order_mg.status_code == 200:
                f.write(str(token_order_mg.json()["access_token"]))
            else:
                print(4)
                raise credentials_exception
            f.close()
            if "access_token" not in token_order_mg.json():
                print(41)
                raise credentials_exception
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post("/register")
async def register(form_data: User):
    """
    Registers a new user.

    Args:
        form_data: A User object containing user information.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 400: If a user with the same username already exists.
    """
    # Also create account in the microservices
    token_livestock_id = requests.post(config.get("LIVESTOCK_ID_URL") + "/register", json=form_data)
    token_order_mg = requests.post(config.get("ORDER_MANAGEMENT_URL") + "/users/", json=form_data + {"email": form_data.username + "@gmail.com"})
    
    user = db.get_user_by_username(form_data.username)
    if token_livestock_id.status_code != 200 or token_order_mg.status_code != 201 or user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    form_data.password = pwd_context.hash(form_data.password)
    _id = db.create_user(form_data.to_db())
    return {"message": f"User created successfully with ID {_id}"}
