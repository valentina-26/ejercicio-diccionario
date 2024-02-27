productos_pan = {
    "pan_integral": {"precio": 1.5, "descripcion": "Pan integral"},
    "pan_frances": {"precio": 1.0, "descripcion": "Pan francés"},
    "pan_molde": {"precio": 2.0, "descripcion": "Pan de molde"}
}

productos_pasteles = {
    "pastel_chocolate": {"precio": 15.0, "descripcion": "Pastel de chocolate"},
    "pastel_vainilla": {"precio": 12.0, "descripcion": "Pastel de vainilla"},
    "pastel_zanahoria": {"precio": 18.0, "descripcion": "Pastel de zanahoria"}
}

productos_bolleria = {
    "croissant": {"precio": 1.8, "descripcion": "Croissant"},
    "donuts": {"precio": 1.2, "descripcion": "Donuts"},
    "ensaimada": {"precio": 2.5, "descripcion": "Ensaimada"}
}

# Solicitar al cliente que elija una categoría
print("Bienvenido a la panadería kreisel supra, solo por el dia de hoy tenemos promociones en todas nuestras categorias, Por favor elija una categoría de productos:")
print("1. Panes")
print("2. Pasteles")
print("3. Bollería")
opcion = input("Ingrese el número correspondiente a la categoría: ")

# Mostrar los productos de la categoría seleccionada por el cliente

promocion_1=("cualquier producto a tan solo 1.0")
promocion_2=("cualquier producto a tan solo 10.0") 
promocion_3=("cualquier producto a tab solo 1.0")


if opcion == "1":
    print("Productos de pan:")
    for producto, detalles in productos_pan.items():
        print(producto, "-", detalles["descripcion"], "- Precio:", detalles["precio"])
    print("promocion:",promocion_1["panes"])
elif opcion == "2":
    print("Productos de pasteles:")
    for producto, detalles in productos_pasteles.items():
        print(producto, "-", detalles["descripcion"], "- Precio:", detalles["precio"])
    print("promocion:",promocion_2["pasteles"])
elif opcion == "3":
    print("Productos de bollería:")
    for producto, detalles in productos_bolleria.items():
        print(producto, "-", detalles["descripcion"], "- Precio:", detalles["precio"])
    print("promocion:", promocion_3["Bolleria"])
else:
    print("Opción no válida. Por favor, seleccione una opción válida (1, 2 o 3).")
