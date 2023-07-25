import json

def convert_geometry(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    converted_data = {
        "format_version": data["format_version"],
        "minecraft:geometry": []
    }

    for geometry in data["minecraft:geometry"]:
        converted_geometry = {
            "description": geometry["description"],
            "bones": []
        }

        for bone in geometry["bones"]:
            if "cubes" in bone:
                cubes = bone.pop("cubes")
                bone_name = bone["name"]
                bone_parent = bone.get("parent")
                bone_pivot = bone.get("pivot")
                converted_geometry["bones"].append(bone)

                # Create an empty "cubes" list for the original bone
                bone["cubes"] = []

                for i, cube in enumerate(cubes):
                    cube_rotation = cube.get("rotation")
                    if cube_rotation is None:
                        # If cube has no rotation, add it to the existing bone
                        bone["cubes"].append(cube)
                    else:
                        # Otherwise, create a new cube bone
                        cube_bone = {
                            "name": f"cube{i + 1}",
                            "parent": bone_name,
                            "pivot": cube.get("pivot", bone_pivot),
                            "rotation": cube_rotation,
                            "cubes": [
                                {
                                    "origin": cube.get("origin", [0, 0, 0]),
                                    "size": cube.get("size", [0, 0, 0]),
                                    "inflate": cube.get("inflate", 0),
                                    "uv": cube.get("uv", [0, 0])
                                }
                            ]
                        }
                        converted_geometry["bones"].append(cube_bone)

            else:
                converted_geometry["bones"].append(bone)

        converted_data["minecraft:geometry"].append(converted_geometry)

    with open(output_file, 'w') as file:
        json.dump(converted_data, file, indent=4)

convert_geometry("geometry_1_scaled.json", "geometry_2_added_groups_and_cube_properties.json")
