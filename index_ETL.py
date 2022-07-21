from datetime import datetime

from extract_data import extrac_data_zip, extract
from transform_data import transform
from load_data import load

# Logging function


def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + ', ' + message + '\n')


def etl():
    log("Extract phase Started")
    extrac_data_zip()
    extracted_data = extract()
    log("Extract phase Ended")

    log("Transform phase Started")
    transform_data = transform(extracted_data)
    log("Transform phase Ended")

    log("Load phase Started")
    load('transformed_data.csv', transform_data)
    log("Load phase Ended")


if __name__ == '__main__':
    log("ETL Job Started")
    print("ETL Job Started")
    etl()
    log("ETL Job Ended")
    print("ETL Job Ended")
