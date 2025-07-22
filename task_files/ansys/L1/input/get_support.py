import traceback

output_path = "C:/Users/Docker/Downloads/support.txt"

try:
    with open(output_path, "w") as f:
        all_objects = ExtAPI.DataModel.Tree.AllObjects

        support_obj = None
        for obj in all_objects:
            if obj.Name == 'Fixed Support':
                support_obj = obj
            
        f.write('Geometry: {} Face'.format(str(support_obj.Location.Ids.Count)))
        

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())


