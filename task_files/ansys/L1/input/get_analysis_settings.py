import traceback

output_path = "C:/Users/Docker/Downloads/analysis_settings.txt"

try:
    with open(output_path, "w") as f:
        all_objects = ExtAPI.DataModel.Tree.AllObjects
        ana_obj = None
        for obj in all_objects:
            if obj.Name == 'Analysis Settings':
                ana_obj = obj

        f.write(str(ana_obj.StepEndTime))
        

except Exception as e:
    with open(output_path, "a") as f:
        f.write("An error occurred:\n")
        f.write(traceback.format_exc())


