import json

def filter_cubes(bones):
    new_bones = []
    for bone in bones:
        if 'cubes' in bone:
            new_cubes = []
            for cube in bone['cubes']:
                cube_size = cube['size']
                if (0 < cube_size[0] < 0.999999) or (0 < cube_size[1] < 0.999999) or (0 < cube_size[2] < 0.999999):
                    new_cubes.append(cube)
            bone['cubes'] = new_cubes
        new_bones.append(bone)
    return new_bones

# Archivo de entrada
input_file = 'geometry.json'
# Archivo de salida
output_file = 'geometry_manual_adjust.json'

with open(input_file, 'r') as file:
    data = json.load(file)

geometry = data['minecraft:geometry']
for geo in geometry:
    bones = geo['bones']
    geo['bones'] = filter_cubes(bones)

with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)
