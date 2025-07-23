import traceback

output_path = "C:/Users/Docker/Downloads/pressure_info.txt"

try:
    with open(output_path, "w") as f:
        all_objects = ExtAPI.DataModel.Tree.AllObjects
        pressure_obj = None
        for obj in all_objects:
            if 'Pressure' in obj.Name:
                pressure_obj = obj
            
        f.write(str(pressure_obj.Location.Ids.Count)+'\n')
        f.write(str(pressure_obj.Magnitude)+'\n')
        

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())

