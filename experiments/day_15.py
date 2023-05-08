import glob
import csv
import shutil


def test_blob_module():
    my_files = glob.glob("../files/*.txt")
    print(my_files)
    for file_path in my_files:
        with open(file_path, 'r') as file:
            print(file.read().upper())


def test_csv_module():
    with open("../files/weather.csv") as csv_file:
        data = list(csv.reader(csv_file))
        print(data)
    city = input("type City Name for get temperature: ")

    for row in data[1:]:
        if row[0] == city:
            print(row[1])

def test_shutil():
    # shutil permite crear zips de manera muy sencilla
    shutil.make_archive("output", "zip", "../files")


test_shutil()