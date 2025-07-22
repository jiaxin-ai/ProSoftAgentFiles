import traceback

output_path = "C:/Users/Docker/Downloads/material.txt"

try:
    with open(output_path, "w") as f:
        geometry = ExtAPI.DataModel.Project.Model.Geometry
        all_bodies = ExtAPI.DataModel.GetObjectsByType(DataModelObjectCategory.Body)
        body = all_bodies[0]
        f.write(body.Material)

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())
