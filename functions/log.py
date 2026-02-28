from datetime import datetime
import os

base_dir        = os.path.dirname(os.path.dirname(__file__))
caminho_debug   = os.path.join(base_dir, "debug.txt")

def log(msg):
    
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(caminho_debug, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{agora}] {msg}\n")