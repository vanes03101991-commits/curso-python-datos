#1 Crear el diccionario con los datos de prueba 
solicitud = {
"codigo": "ADM-004",
"tipo": "Actualizacion de datos",
"area_solicitante": "Talento Humano",
"dias_pendiente": 3,
"afecta_operacion":True,
"estado": "Pendiente", 
}
#2. Consultar los datos que se van a evaluar
estado = solicitud["estado"]
dias_pendiente = solicitud["dias_pendiente"]
afecta_operacion = solicitud["afecta_operacion"]

# 3 y 4. Evaluar reglas en orden estricto y asignar clasificacion + accion
if estado == "cerrada":
   clasificacion = "CERRADA" 
   accion = "Registrar que no quiere nueva gestion."
elif afecta_operacion and dias_pendiente >= 2:
   clasificacion = "URGENTE"
   accion = "Escalar al responsable para atencion prioritaria."
elif afecta_operacion or dias_pendiente >= 5:
   clasificacion = "PRIORITARIA"
   accion = "Programar atencion preferente."
else: clasificacion = "NORMAL"
accion = "Mantener en el flujo habitual de atencion."

# 5. Mostrar el resumen con una f-string
print("--- Resumen de evaluacion ---")
print(f"Codigo:    {solicitud["codigo"]}")
print(f"Tipo:      {solicitud["tipo"]}")
print(f"Estado:    {estado}")
print(f"Clasificacion:  {clasificacion}")
print(f"Accion sugerida:{accion}")


