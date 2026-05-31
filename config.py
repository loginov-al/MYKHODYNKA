import os
from dotenv import load_dotenv


load_dotenv()



# Модули Базы данных PosgreSQL #






# Секретный ключ Flask #
SECRET_KEY=os.environ["SECRET_KEY"]