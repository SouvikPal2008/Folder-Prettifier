
import os
from time import sleep as sl


def soldier(path, file, format):
    # path = fr"{Path}"
    global input
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"Episode {i}{format}")
            i += 1
    sl(2)
    print("Capitalization Was Successful....")
    sl(2)
    print("Image Rename Was Successful..")
    sl(1)
    print("Process Was Successful Please Check Your Folder")
    print(
        "If You Find Any Problem Then Refresh The Folder Or run The Program Again by Pressing 1 Otherwise Press 0")
    runner = int(input("Enter Here : "))
    if runner == 1:
        soldier(path, file, format)
    else:
        print("Thank You For Using Our Service")


soldier(r"D:\Movies\Web Series\Panchayat Season 02", r"D:\coding\PythonTutorials\Exercises, Problems, Challenges, Quizes\Exercice_08file",
        ".mkv")
