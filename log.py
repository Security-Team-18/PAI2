from datetime import datetime

def log(transaccion, valor):
    
    now = datetime.now()
    fecha=now.strftime("%d/%m/%Y %H:%M:%S")
    with open("./almacenamiento/log.txt", 'a') as file:
        file.writelines(fecha+ " -> Transacción " + transaccion + " no íntegra \n")