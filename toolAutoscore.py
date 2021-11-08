import sys
import os
import shutil
import subprocess
import warnings
import glob
from datetime import datetime
warnings.filterwarnings('ignore')

# Get path test script
path_script = "./test_script/"

# Get path test case
path_test_case = "./test_case"

# Get test script file
baiSV = glob.glob(os.path.join(path_script, "*"))

# Get test case
test_case = glob.glob(os.path.join(path_test_case, "*", "input"))

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
date_time_file = now.strftime("%d%m%Y_%H%M%S")
date_time_csv = now.strftime("%d/%m/%Y %H:%M:%S")

# Write score to file .csv
f = open("./test_report/pointSheet.csv", "w")
f.write("Student ID" + "," + "Test Case" + "," + "Result" + "\n")
f.close()

for subfolder in test_case:
    for stuID in baiSV:
        if stuID.endswith(".c"):
            shutil.copy2(stuID, subfolder)
            # Run file code and write resuls to file
            subprocess.call(["gcc", stuID])  # Compile MSSV.c
            StudentID = stuID.split('.c')[0]  # Get Student ID from file.
            # 0 : program can compile, 1: program can not compile
            if subprocess.call(["gcc", stuID]) == 0:
                answer = 0
                args = []
                args.append("./a.exe")

                result = subprocess.run(
                    args, capture_output=True, text=True, timeout=10)
                result = str(result.stdout)
                f = open("./test_report/pointSheet.csv", "a")
                f.write(StudentID + "," + str(subfolder) + "," + result + "\n")
                f.close()
            if "a.exe" in subfolder:
                os.remove("a.exe")
print("\n\nCompleted")
