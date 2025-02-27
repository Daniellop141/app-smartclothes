import re

# simulacion con las prendas disponibles
inventario = [
    {"dato": "Camiseta Negra", "talla": "M", "color": "Negro", "precio": 25000},
    {"dato": "Jean Azul", "talla": "L", "color": "Azul", "precio": 75000},
    {"dato": "Sudadera Gris", "talla": "M", "color": "Gris", "precio": 90000},
    {"dato": "Zapatos Deportivos", "talla": "42", "color": "Blanco", "precio": 150000},
    {"dato": "Chaqueta Roja", "talla": "L", "color": "Rojo", "precio": 120000},
    {"dato": "Vestido Verde", "talla": "S", "color": "Verde", "precio": 85000},
    
]

# Función para recomendar prendas según los filtros ingresados por el usuario
def recomendar_ropa(dato=None, talla=None, color=None):
    liga = [articulo for articulo in inventario if (dato in articulo["dato"].lower() if dato else True)
                        and (articulo["talla"].lower() == talla if talla else True)
                        and (articulo["color"].lower() == color if color else True)]
    return liga


def version_interactiva():
    try:
        entrada_usuario = input("Ingrese el producto que busca con talla y color (Ejemplo: 'producto-color-talla'): ").lower()
        palabras = entrada_usuario.split()
        
        colores = {"negro", "azul", "gris", "blanco", "rojo", "verde"}
        tallas = {"s", "m", "l", "xl", "42", "única"}
        
        color = next((p for p in palabras if p in colores), None)
        talla = next((p for p in palabras if p in tallas), None)
        dato = " ".join([p for p in palabras if p not in colores and p not in tallas]).strip()
        
        resultado = recomendar_ropa(dato, talla, color)
        
        print("\nResultados de búsqueda:")
        if resultado:
            for prenda in resultado:
                print(f"- {prenda['dato']} | Talla: {prenda['talla']} | Color: {prenda['color']} | Precio: ${prenda['precio']}")
        else:
            print(f"No se encontraron resultados para '{entrada_usuario}'. Producto no disponible.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    version_interactiva()

