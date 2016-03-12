from os.path import isfile
from json import dump, load
import openpyxl as xl


def excel_to_json(filename):
    workbook = xl.load_workbook(filename + '.xlsx', read_only=True)
    data_worksheet = workbook['All DATA']

    rows = []

    for row in data_worksheet.rows:
        plot = row[0].value
        species = row[1].value
        doy = row[2].value
        num_flowers = row[3].value
        year = row[4].value
        habitat = row[5].value

        if plot == 'PLOT':
            continue  # skip title row

        rows.append([plot, species, doy, num_flowers, year, habitat])

    with open(filename + '.json', 'w') as outfile:
        dump(rows, outfile)


def read_json(filename):
    with open(filename + '.json') as json_data:
        return load(json_data)


if __name__ == '__main__':
    file_name = 'phenology_data_1973_2012'

    if not isfile(file_name + '.json'):
        excel_to_json(file_name)

    data = read_json(file_name)
