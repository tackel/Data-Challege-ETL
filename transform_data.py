import pandas as pd


def transform(data):
    # Convert height which is in inches to millimeter
    # Convert weight which is in pounds to kilograms
    # Convert the datatype of the column into float
    data[['height', 'weight']] = data[['height', 'weight']].astype(float)
    # Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
    data['height'] = round(data.height * 0.0254, 2)

    # Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
    data.weight = round(data.weight * 0.45359237, 2)

    return data
