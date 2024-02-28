eleccion_principal=input("bienvenido a la panaderia kreisel supra,por favor elija el tipo de producto que desea adquirir:pan, bolleria o reposteria?")
if eleccion_principal == "pan":
    productos_panaderia =tuple((
        "baguette",
        "pan de molde",
        "pan integral",
        "pan de centeno",
        "bagel",
        "pan de ajo",
        "panecillos",
        "pan de hamburguesa",
        "pan de pita",
        "panecillos de leche",
        "promocion pan de ajo + bagel",
        "promocion bagel + panecillos de leche"
        ))
    precios_panaderia=tuple((
        4000,
        3000,
        2500,
        2500,
        3200,
        2500,
        3000,
        2200,
        3000,
        2800,
        4000,
        4000
            ))
    for i,val in enumerate(productos_panaderia):
       print(f"""{i}.{val} ${precios_panaderia[i]}""")

    eleccion=int(input())
    num_productos=int(input("cuantos desea?"))
    print(f"usuario usted selecciono el producto {productos_panaderia[eleccion]}con un valor de ${precios_panaderia[eleccion]*num_productos}")
    dinero=int(input("escriba la cantidad de dineo con la que cuenta: $"))
    vueltos=dinero - (precios_panaderia[eleccion]*num_productos)
    falta=(precios_panaderia[eleccion]*num_productos)-dinero
    if dinero >= precios_panaderia[eleccion]*num_productos:
       print("si le alcanza para el producto que desea,sus vueltas son $", vueltos)
    else:
       print("no le alcanza para el producto que desea,le faltan $",falta)

elif eleccion_principal == "bolleria":
    productos_bolleria=tuple(("""
    "Croissant",
    "ensaimada",
    "napolitana de crema",
    "palmera de chocolate",
    "palmera de coco",
    "palmera de crema",
    "chapata de chocolate",
    "bollo de leche",
    "churros", 
    "rosquillas",
    "promocion churros + ensaimada",
    "promocion bollo de leche+palmera de chocolate"
    """))
    precios_bolleria = tuple((
    3000,
    5000,
    4800,
    4000,
    4000,
    4000,
    3500,
    2500,
    3000,
    3200,
    3500,
    2000
    ))

    for i,val in enumerate(productos_bolleria):
        print(f"""{i}.{val} ${precios_bolleria}[i]""")

    eleccion=int(input())
    num_productos=int(input("cuantos desea?"))
    print(f"usuario usted selecciono el producto {productos_bolleria[eleccion]}con un valor de ${precios_bolleria[eleccion]*num_productos}")
    dinero=int(input("escriba la cantidad de dineo con la que cuenta: $"))
    vueltos=dinero - (precios_bolleria[eleccion]*num_productos)
    falta=(precios_bolleria[eleccion]*num_productos)-dinero
    if dinero >= precios_bolleria[eleccion]*num_productos:
        print("si le alcanza para el producto que desea,sus vueltas son $", vueltos)
    else:
        print("no le alcanza para el producto que desea,le faltan $",falta)

elif eleccion_principal=="reposteria":
    productos_reposteria=tuple((
    "tarta de manzana",
    "Brownie",
    "mufin",
    "cookies",
    "tarta de fresa",
    "tarta de chocolate",
    "tarta de limon",
    "coulante de chocolate",
    "eclair",
    "tarta de almendra",  
    "promocion brownie + cookies",
    "tarta de almendra + muffin",
    ))
    precios_reposteria=tuple((
    3000,
    2000,
    1500,
    500,
    4500,
    4500,
    4500,
    5000,
    3500,
    4500,
    5000,
    5000,
    ))
    for i,val in enumerate(productos_reposteria):
        print(f""" {i}. {val} ${precios_reposteria[i]}""")
        
    eleccion=int(input())
    num_productos=int(input("cuantos desea?"))
    print(f"usuario usted selecciono el producto {productos_reposteria[eleccion]}con un valor de ${precios_reposteria[eleccion]*num_productos}")
    dinero=int(input("escriba la cantidad de dineo con la que cuenta: $"))
    vueltos=dinero - (precios_reposteria[eleccion]*num_productos)
    falta=(precios_reposteria[eleccion]*num_productos)-dinero
    if dinero >= precios_reposteria[eleccion]*num_productos:
        print("si le alcanza para el producto que desea,sus vueltas son $", vueltos)
    else:
        print("no le alcanza para el producto que desea,le faltan $",falta)
        