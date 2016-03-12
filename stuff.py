import openpyxl as xl

# columns
PLOT = 0
SPECIES = 1
DOY = 2
NUM_FLOWERS = 3
YEAR = 4
HABITAT = 5


def read_data(filename='phenology_data_1973_2012.xlsx'):
    wb = xl.load_workbook(filename, read_only=True)
    ws = wb['All DATA']

    for row in ws.rows:
        plot = row[PLOT].value
        species = row[SPECIES].value
        doy = row[DOY].value
        num_flowers = row[NUM_FLOWERS].value
        year = row[YEAR].value
        habitat = row[HABITAT].value

        if plot == 'PLOT':
            continue  # skip title row


if __name__ == '__main__':
    read_data()
