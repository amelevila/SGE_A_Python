from cotxe import Cotxe
from colibri import Colibri

# 3 instàncies de Cotxe
cotxe1 = Cotxe("Toyota", "Corolla", 2022, "Blanc", 20000)
cotxe2 = Cotxe("Ford", "Focus", 2021, "Negre", 18000)
cotxe3 = Cotxe("Honda", "Civic", 2023, "Blau", 22000)

# 3 instàncies de Colibrí
colibri1 = Colibri("Rubí", "Petit", 50, "Verd", "Selva")
colibri2 = Colibri("Anna", "Mitjà", 55, "Vermell", "Bosc")
colibri3 = Colibri("Blauet", "Petit", 45, "Blau", "Muntanya")

# Mostrar 3 getters de Cotxe
print("Informació de Cotxe:")
print("Marca:", cotxe1.get_marca())
print("Model:", cotxe1.get_model())
print("Color:", cotxe1.get_color())

# Mostrar 4 getters de Colibrí
print("\nInformació de Colibrí:")
print("Espècie:", colibri1.get_especie())
print("Mida:", colibri1.get_mida())
print("Velocitat:", colibri1.get_velocitat())
print("Hàbitat:", colibri1.get_habitat())

# Modificar 2 atributs de Cotxe a través dels setters
cotxe1.set_color("Vermell")
cotxe1.set_preu(21000)

# Mostrar els 2 atributs modificats a través dels getters
print("\nCotxe modificat:")
print("Nou color:", cotxe1.get_color())
print("Nou preu:", cotxe1.get_preu())

# Modificar 2 atributs de Colibrí a través dels setters
colibri1.set_velocitat(60)
colibri1.set_color("Groc")

# Mostrar els 2 atributs modificats a través dels get
print("\nColibrí modificat:")
print("Nova velocitat:", colibri1.get_velocitat())
print("Nou color:", colibri1.get_color())
