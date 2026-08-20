from pathlib import Path

ruta = Path("datos/mediciones.csv")

lineas = ruta.read_text(encoding="utf-8").strip().splitlines()
datos = []

for linea in lineas[1:]:
    tiempo, posicion = linea.split(",")
    datos.append((float(tiempo), float(posicion)))

promedio = sum(posicion for _, posicion in datos) / len(datos)

print(f"Número de mediciones: {len(datos)}")
print(f"Posición promedio: {promedio:.3f}")
