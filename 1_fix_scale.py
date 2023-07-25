import json

# Lee el archivo geometry.json
with open('geometry.json', 'r') as file:
    data = json.load(file)

# Recorre la estructura de datos y modifica los valores de 'size' si están entre 0 y 1
for geometry in data['minecraft:geometry']:
    for bone in geometry['bones']:
        if 'cubes' in bone:
            for cube in bone['cubes']:
                size = cube.get('size', [])
                if len(size) == 3:
                    size = [1 if 0 <= value <= 1 else value for value in size]
                    cube['size'] = size

# Crea el nuevo archivo geometry_1_scaled.json con los cambios aplicados
with open('geometry_1_scaled.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Skip this one step if not working with 4D Skins, but rename your geometry to geometry_1_scaled.json")