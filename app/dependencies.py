from fastapi import Header, HTTPException, Depends


def get_token_header(x_token: str = Header("")):
    if x_token != "":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


def get_query_token(token: str):
    if token != "":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return current_user
