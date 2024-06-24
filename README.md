This template is used for developing Telegram bots using the `aiogram v3.0+` library [Source 8](https://docs.aiogram.dev/uk_UA/latest/index.html).
## SQLAlchemy + Alembic
The code includes examples of a User table using SQLAlchemy 2.0, and scripts for Alembic (Alembic initialization, creation and application of migrations).

But if you have never worked with these tools, refer to the documentation and learn about these tools. I also have an English [course on these tools on Udemy](https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126).

![img.png](https://img-c.udemycdn.com/course/240x135/5320614_a8af_2.jpg)

### To start using:
1. Copy `.env.dist` to `.env` and fill in the necessary data.
2. Create new handlers.
3. **Docker:**
  1. You can run the project with Docker right away, and if you don't have it, [download and install](https://docs.docker.com/get-docker/).
  2. Run the project with the command `docker-compose up`
4. **Without Docker:**
  1. Create a [venv](https://docs.python.org/3/library/venv.html)
  2. Install dependencies from requirements.txt: `pip install -r requirements.txt --pre`
  3. Run the project with the command `python3 bot.py`

### How to make and register handlers:
You create a `you_name.py` module in the `handlers` folder.

You create a router in `you_name.py`.
```python
from aiogram import Router
user_router = Router()
```
You can make several routers in one module, and attach handlers to each of them.
You can register handlers with decorators:
```python
@user_router.message(commands=["start"])
async def user_start(message):
   await message.reply("Welcome, ordinary user!")
```

Go to the `bot.py` file and add all routers to it:
```python
from tgbot.handlers.admin import admin_router
from tgbot.handlers.echo import echo_router
from tgbot.handlers.user import user_router

...

async def main():

    ...

   dp.include_routers(*routers_list)

    ...
```
### How to Launch the Database and Perform Your First Migration:

1. Go to the `.env` file and fill in the database information if you haven't already done so.

2. Go to the `docker-compose.yml` file and uncomment the sections: `api`, `pg_database`, and `volumes` to get started.

3. Go to `config.py` and complete the `TODO` in the `construct_sqlalchemy_url` function. Also, find the `load_config` function and uncomment the line that initializes the database configuration `db=DbConfig.from_env(env)` to activate the database connection.

4. Now we can restart Docker with the new containers using the command:

    `docker-compose up --build.`

5. Everything is ready! Now we can perform the migration! Open the terminal and enter the following command:

    `docker-compose exec api alembic upgrade head`

### aiogram v3 Tutorials
There are no videos yet, but @Groosha has already started making [his guide](https://mastergroosha.github.io/aiogram-3-guide).
