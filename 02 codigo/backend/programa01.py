import random
import os

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    Limite_n_valores_vector = 20
    min_val_aleatorio = 1
    max_val_aleatorio = 500
    
    resultados = {}
    opcion_de_menu = '9'

    vector_num_aleatorios = []
    for _ in range(Limite_n_valores_vector):
        vector_num_aleatorios.append(random.randint(min_val_aleatorio, max_val_aleatorio))

    while opcion_de_menu != '4':
        contador_temporal_resultados = 0

        print("\n\t" + "~"*60, f"N={Limite_n_valores_vector}, Valores (Min={min_val_aleatorio}, Max={max_val_aleatorio})")
        print("\n\tVector generado:", vector_num_aleatorios)

        print("\n\t\t** MENÚ DE OPCIONES **")
        print("\t" + "~"*60)
        print(f"\n\t1. Suma de números del vector: \t\t\t{resultados.get('suma', 'No calculado')}")
        print("\t4. Salir.")
        print("\t" + "~"*60)
        opcion_de_menu = input("\n\tSeleccione una opción: ")

        if opcion_de_menu == '1':
            resultados['suma'] = sum(vector_num_aleatorios)
            print(f"\n-> Suma calculada: {resultados['suma']}")

        elif opcion_de_menu == '4':
            print("\n\t-- Fin del ejercicio -- GRACIAS!!")
            
        else:
            print("* "*15, "Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()