from validaciones import (  
# Importa funciones del archivo validaciones.py para utilizarlas en este archivo.
    validar_texto_obligatorio,  
    # Importa la función que comprueba que un campo no esté vacío.
    validar_dni,  
    # Importa la función que comprueba que el DNI tenga 8 dígitos.
    validar_fecha  
    # Importa la función que comprueba que la fecha sea válida.
)

from archivos import guardar_expedientes  
# Importa la función que permite guardar los expedientes en el archivo CSV.


def registrar_expediente(expedientes):  
# Define una función que recibe la lista de expedientes y permite registrar uno nuevo.
    print("\n--- REGISTRO DE EXPEDIENTE ---")  
    # Muestra el título de la sección de registro; \n genera un salto de línea.

    dni = input("DNI: ").strip()  
    # Solicita el DNI al usuario y elimina los espacios al principio y al final.
    nombre = input("Nombre del ciudadano: ").strip()  
    # Solicita el nombre del ciudadano y elimina los espacios externos.
    fecha = input("Fecha (DD/MM/AAAA): ").strip()  
    # Solicita la fecha y elimina los espacios externos.
    asunto = input("Asunto: ").strip() 
     # Solicita el asunto del expediente y elimina los espacios externos.
    area = input("Area de destino: ").strip()  
    # Solicita el área de destino y elimina los espacios externos.

    if not all([  
    # Comprueba si todos los elementos de la lista cumplen las condiciones; 
    # not invierte el resultado de all().
        validar_texto_obligatorio(dni),  # Comprueba que el DNI no esté vacío.
        validar_texto_obligatorio(nombre),  # Comprueba que el nombre no esté vacío.
        validar_texto_obligatorio(fecha),  # Comprueba que la fecha no esté vacía.
        validar_texto_obligatorio(asunto),  # Comprueba que el asunto no esté vacío.
        validar_texto_obligatorio(area)  # Comprueba que el área no esté vacía.
    ]):
        print("Error: todos los campos son obligatorios.")  
        # Muestra un mensaje indicando que falta completar algún campo.
        return  # Termina la función sin registrar el expediente.

    if not validar_dni(dni):  # Comprueba si el DNI no cumple la validación establecida.
        print("Error: el DNI debe contener 8 digitos.")  
        # Informa que el DNI debe tener exactamente 8 números.
        return  # Termina la función para impedir que se registre un DNI incorrecto.

    if not validar_fecha(fecha):  # Comprueba si la fecha ingresada no es válida.
        print("Error: la fecha no es válida.")  
        # Muestra un mensaje indicando que la fecha es incorrecta.
        return  # Termina la función para impedir el registro de una fecha inválida.

    numero = max( 
        # Obtiene el número más alto de los códigos existentes para generar el siguiente.
        [int(e["codigo"].split("-")[1]) for e in expedientes],  
        # Crea una lista con la parte numérica de cada código; 
        # split("-") separa el código por el guion e 
        # int() convierte el resultado en entero.
        default=0  
        # Si la lista está vacía, max() devuelve 0 en lugar de producir un error.
    ) + 1  # Suma 1 al número más alto para obtener el siguiente número de expediente.

    expediente = {  
    # Crea un diccionario que almacenará los datos del nuevo expediente.
        "codigo": f"EXP-{numero:04d}",  
        # Genera un código con el prefijo EXP- y cuatro dígitos; por ejemplo, EXP-0001.
        "dni": dni,  
        # Guarda el DNI ingresado por el usuario.
        "nombre": nombre,  
        # Guarda el nombre del ciudadano.
        "fecha": fecha,  
        # Guarda la fecha del expediente.
        "asunto": asunto,  
        # Guarda el asunto del expediente.
        "area": area  
        # Guarda el área de destino.
    }  # Finaliza la creación del diccionario.

    expedientes.append(expediente)  
    # Agrega el nuevo diccionario al final de la lista de expedientes.
    guardar_expedientes(expedientes)  
    # Guarda la lista actualizada en el archivo CSV.

    print("Expediente registrado:", expediente["codigo"])  
    # Muestra un mensaje de confirmación junto con el código generado.

# FUNCIÓN: registrar_expediente(expedientes)
# Solicita los datos del ciudadano, valida que sean correctos, genera un código único consecutivo,
# agrega el expediente a la lista y guarda todos los registros actualizados en el archivo CSV.


def buscar_expediente(expedientes):  
    # Define una función que recibe la lista de expedientes y permite buscar uno 
    # por su código.
    codigo = input("Codigo del expediente: ").strip().upper()  
    # Solicita el código, elimina espacios externos y convierte las letras a mayúsculas.

    for expediente in expedientes:  
    # Recorre cada diccionario de la lista de expedientes.
        if expediente["codigo"] == codigo:  
        # Compara el código buscado con el código del expediente actual.
            print(expediente)  # Muestra todos los datos del expediente encontrado.
            return expediente  
        # Devuelve el diccionario del expediente encontrado y termina la función.

    print("No se encontro el expediente.")  
    # Se ejecuta si el ciclo termina sin encontrar coincidencias.
    return None  
    # Devuelve None para indicar que no se encontró ningún expediente.

# FUNCIÓN: buscar_expediente(expedientes)
# Solicita un código y recorre la lista buscando un expediente que tenga ese mismo código.
# Si lo encuentra, muestra y devuelve sus datos; si no, devuelve None.


def listar_expedientes(expedientes):  
    # Define una función que recibe la lista de expedientes y permite mostrar 
    # todos sus registros.
    if not expedientes:  
        # Comprueba si la lista está vacía; una lista vacía se interpreta como False.
        print("No hay expedientes registrados.")  
        # Informa que no existen expedientes registrados.
        return  # Termina la función porque no hay registros que mostrar.

    for expediente in expedientes:  # Recorre cada expediente almacenado en la lista.
        print(expediente)  # Muestra el diccionario correspondiente al expediente actual.

# FUNCIÓN: listar_expedientes(expedientes)
# Muestra todos los expedientes registrados.
# Si la lista está vacía, informa al usuario y termina la función.


def ordenar_expedientes(expedientes):  
    # Define una función que recibe la lista de expedientes y permite ordenarla.
    expedientes.sort(key=lambda e: e["codigo"])  
    # Ordena la lista utilizando el código como criterio; 
    # lambda crea una función anónima que recibe cada expediente y devuelve su código.
    guardar_expedientes(expedientes)  
    # Guarda en el CSV la lista después de haber sido ordenada.
    print("Expedientes ordenados por codigo.")  
    # Informa que los expedientes fueron ordenados correctamente.

# FUNCIÓN: ordenar_expedientes(expedientes)
# Ordena los expedientes según su código, guarda el nuevo orden en el archivo CSV y muestra un mensaje de confirmación.
