import pandas as pd
import requests
import zipfile
import glob
import xml.etree.ElementTree as ET
from datetime import datetime


def extrac_data_zip():
    """
    Function for extract all folder and files from the .zip file to use in the tasks 
    """
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip'
    req = requests.get(url)
    if req.status_code == 200:
        open('sourcefiles.zip', 'wb').write(req.content)

    with zipfile.ZipFile('sourcefiles.zip', 'r') as zip_ref:
        zip_ref.extractall('data')


def extract_from_csv(file_to_process):
    """csv extract function"""
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    """ json extract function """
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    """ xml extract function """
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        df = pd.DataFrame(
            [{"name": name, "height": height, "weight": weight}])
        dataframe = pd.concat([dataframe, df], ignore_index=True)

    return dataframe


def extract():
    # process all csv files
    # for csvfile in glob.glob("data/*.csv"):
    #    extracted_data = extracted_data.append(
    #        extract_from_csv(csvfile), ignore_index=True)
    dataframe1 = extract_from_csv("data/source1.csv")

    dataframe2 = extract_from_json('data/source2.json')

    dataframe3 = extract_from_xml('data/source3.xml')

    extracted_data = pd.concat(
        [dataframe1, dataframe2, dataframe3], ignore_index=True)

    return extracted_data
