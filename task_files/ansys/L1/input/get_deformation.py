import traceback

output_path = "C:/Users/Docker/Downloads/total_deformation.txt"

try:
    with open(output_path, "w") as f:
        all_objects = ExtAPI.DataModel.Tree.AllObjects

        total_deform_obj = None
        for obj in all_objects:
            if obj.Name == 'Total Deformation':
                total_deform_obj = obj
                
        if total_deform_obj is not None:
            f.write('Total Deformation Exists')
        else:
            f.write('None')
        

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())



