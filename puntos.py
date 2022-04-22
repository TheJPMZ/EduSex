import json
import random

def ganar(cantidad_buenas):
    with open('usuario.json', 'r+') as f:
        data = json.load(f)
        
        adicion = cantidad_buenas/5
        if adicion <0.5:
            boost = random.randint(1,3)
        else:
            boost = random.randint(2,5)
        puntos_ganados = int(adicion*boost)
        data['puntos'] += puntos_ganados
        f.seek(0)  # rewind
        json.dump(data, f)
        f.truncate()
        f.close()
        
        

        
def gastar(puntos_a_gastar):
    pass
    
    
    


   