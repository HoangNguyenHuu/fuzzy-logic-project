import xlrd

with xlrd.open_workbook('media/toa-do.xlsx') as book:

    sheet = book.sheet_by_index(1)

    x_coordinate = [x for x in sheet.col_values(1)]
    y_coordinate = [y for y in sheet.col_values(2)]

    MAP_NAVS = []
    for i in range(1, len(x_coordinate)):
        MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))

    for i in range(len(MAP_NAVS)):
        print(MAP_NAVS[i])