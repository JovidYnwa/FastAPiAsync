import asyncclick as click
from db import database
from managers.user import UserManager
from models.enums import RoleType

"""
Example of executing this command
export PYTHONPATH=./
python commands/create_user.py -f TestClick -l Acyncclick -e test@j.com -p 111911919 -i 12344567 -pa jova123
"""

@click.command()
@click.option("-f", "--fist_name", type=str, required=True)
@click.option("-l", "--last_name", type=str, required=True)
@click.option("-e", "--email", type=str, required=True)
@click.option("-p", "--phone", type=str, required=True)
@click.option("-i", "--iban", type=str, required=True)
@click.option("-pa", "--password", type=str, required=True)
async def create_user(fist_name, last_name, email, phone, iban, password):
    user_data = {"first_name": fist_name, "last_name": last_name, "email": email,
                 "phone": phone, "iban": iban, "password": password, "role": RoleType.admin}
    await database.connect()
    await UserManager.register(user_data)
    await database.disconnect()


if __name__ == "__main__":
    create_user(_anyio_backend="asyncio")
