import traceback

output_path = "C:/Users/Docker/Downloads/force_info.txt"

try:
    with open(output_path, "w") as f:
        all_objects = ExtAPI.DataModel.Tree.AllObjects

        force_obj = None
        for obj in all_objects:
            if 'Force' in obj.Name:
                force_obj = obj
        
        f.write('Geometry: {} Face\n'.format(str(force_obj.Location.Ids.Count)))
        f.write(str(force_obj.Magnitude)+'\n')
        

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())



