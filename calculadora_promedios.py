# -*- coding: utf-8 -*-

def ingresar_calificaciones():
    """
    Permite al usuario ingresar materias y sus calificaciones.
    Realiza una validación para asegurar que las calificaciones estén entre 0 y 10.
    Devuelve dos listas: una con los nombres de las materias y otra con las calificaciones.
    """
    materias = []
    calificaciones = []
    
    print("--- Ingreso de Calificaciones ---")
    print("Introduce el nombre de la materia y su calificación (0-10).")
    print("Deja el nombre de la materia en blanco y presiona Enter para finalizar.")
    
    while True:
        nombre_materia = input("\nNombre de la materia: ").strip()
        
        # Si el usuario no introduce nombre, termina el bucle
        if not nombre_materia:
            if not materias:
                print("\nAdvertencia: No se ingresaron datos.")
            break
            
        while True:
            try:
                calificacion_str = input(f"Calificación para '{nombre_materia}': ")
                calificacion = float(calificacion_str)
                
                # Valida que la calificación esté en el rango correcto
                if 0 <= calificacion <= 10:
                    materias.append(nombre_materia)
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10. Inténtalo de nuevo.")
            except ValueError:
                print("Error: Por favor, introduce un número válido para la calificación.")
                
    return materias, calificaciones

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Devuelve 0 si la lista está vacía para evitar errores de división por cero.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado_y_extremos(materias, calificaciones, umbral=5.0):
    """
    Determina qué materias están aprobadas o reprobadas y encuentra
    las materias con la calificación más alta y más baja.
    
    Devuelve:
    - Una lista de tuplas con (materia, calificación, estado).
    - La materia con la calificación más alta.
    - La materia con la calificación más baja.
    """
    if not materias:
        return [], None, None

    # Determinar estado de cada materia
    resultados_detalle = []
    for i in range(len(materias)):
        estado = "Aprobada" if calificaciones[i] >= umbral else "Reprobada"
        resultados_detalle.append((materias[i], calificaciones[i], estado))
        
    # Encontrar extremos
    calificacion_max = max(calificaciones)
    calificacion_min = min(calificaciones)
    
    # Se usan listas por si hay empates en la mejor/peor calificación
    mejores_materias = [materias[i] for i, c in enumerate(calificaciones) if c == calificacion_max]
    peores_materias = [materias[i] for i, c in enumerate(calificaciones) if c == calificacion_min]
    
    materia_max = (", ".join(mejores_materias), calificacion_max)
    materia_min = (", ".join(peores_materias), calificacion_min)
    
    return resultados_detalle, materia_max, materia_min

def mostrar_resumen(promedio, detalles, extremo_max, extremo_min):
    """
    Muestra un resumen final con toda la información procesada.
    """
    print("\n" + "="*40)
    print("📊       RESUMEN ACADÉMICO FINAL       📊")
    print("="*40)
    
    # 1. Promedio General
    print(f"\n✨ Promedio General: {promedio:.2f}")
    
    # 2. Detalle de Materias
    print("\n--- Detalle por Materia ---")
    print(f"{'Materia':<20} | {'Calificación':<12} | {'Estado':<10}")
    print("-" * 50)
    for materia, calificacion, estado in detalles:
        emoji_estado = "✅" if estado == "Aprobada" else "❌"
        print(f"{materia:<20} | {calificacion:<12.2f} | {estado} {emoji_estado}")
    
    # 3. Materias con calificaciones extremas
    if extremo_max and extremo_min:
        print("\n--- Calificaciones Destacadas ---")
        print(f"🏆 Mejor Calificación: {extremo_max[1]:.2f} en '{extremo_max[0]}'")
        print(f"📉 Peor Calificación:  {extremo_min[1]:.2f} en '{extremo_min[0]}'")
    
    print("\n" + "="*40)


def main():
    """
    Función principal que orquesta la ejecución del programa.
    """
    # 1. Ingresar datos
    materias, calificaciones = ingresar_calificaciones()
    
    # 2. Procesar datos solo si se ingresó alguna materia
    if materias:
        # Calcular promedio
        promedio_general = calcular_promedio(calificaciones)
        
        # Determinar estado y encontrar extremos
        UMBRAL_APROBACION = 5.0
        detalles_materias, materia_alta, materia_baja = determinar_estado_y_extremos(
            materias, 
            calificaciones, 
            UMBRAL_APROBACION
        )
        
        # 3. Mostrar el resumen final
        mostrar_resumen(promedio_general, detalles_materias, materia_alta, materia_baja)
    else:
        print("Fin del programa. No se procesó ninguna información.")


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main()
