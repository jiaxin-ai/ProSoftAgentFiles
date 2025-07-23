from pyautocad import Autocad, APoint
import os
import comtypes.client
import math
import time
from shapely.geometry import LineString

def check_autocad_l1_001(dst_file):
    # Open the last recently used file
    acad = Autocad(create_if_not_exists=False)

    try:
        for doc in acad.app.Documents:
            if doc.FullName.lower() == dst_file.lower():
                acad.app.ActiveDocument.Close(False)
                return True
        acad.app.ActiveDocument.Close(False)
        return False
    except Exception as e:
        print(e)
        acad.app.ActiveDocument.Close(False)
        return False

if __name__ == '__main__':
    res = check_autocad_l1_001('AutoCAD_L1_001.dwg')
    with open('C:/Users/Docker/Downloads/AutoCAD_res.txt','w') as f:
        f.write(str(res))
