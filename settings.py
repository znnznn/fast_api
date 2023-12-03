from decouple import config

SECRET_KEY = config("SECRET_KEY", cast=str)

DB_USER = config("DB_USER", cast=str, default="postgres")
DB_PASS = config("DB_PASS", cast=str, default="postgres")
DB_HOST = config("DB_HOST", cast=str, default="localhost")
DB_PORT = config("DB_PORT", cast=int, default=5432)
DB_NAME = config("DB_NAME", cast=str, default="stock")

TRADIER_TOKEN = config("TRADIER_TOKEN", cast=str)

GOOGLE_API_DEVELOPER_KEY = config("GOOGLE_API_DEVELOPER_KEY", cast=str)
GOOGLE_API_CX = config("GOOGLE_API_CX", cast=str)


