#===============================
#===============================
# este codigo va en el .py para no llamar directo la api en el codigo
# va cifrado en el .env
#===============================
#==============================



from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

print("Mi clave es:", api_key)