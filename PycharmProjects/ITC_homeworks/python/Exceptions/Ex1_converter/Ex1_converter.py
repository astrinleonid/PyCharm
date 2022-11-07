import csv

CONV_CEFFICIENT = 3.2808399


def open_and_read_csv(filename):
    """
    Opens csv file, returns the data as array (one column, numbers only)
    """
    try:
        csv_file = open(filename,'r')
    except FileNotFoundError as er:
        raise FileNotFoundError("File " + filename + " not found. Please check the path you provided. ")
    try:
        return read_csv(csv_file)
    except TypeError as er:
        raise TypeError(er)
    except ValueError as er:
        raise ValueError(er)
    finally:
        csv_file.close()

def read_csv(file):
    """
    Reads csv file, returns the data as array (one column, numbers only)
    """
    csv_reader = csv.reader(file, delimiter=',')
    header = []
    header = next(csv_reader, None)
    if len(header) > 30:
        raise TypeError("Wrong format, header too long")
    data = []
    for row in csv_reader:
        if len(row) > 1:
            raise TypeError("Wrong format, should be one column")
        try:
            value = float(row[0])
        except ValueError as error:
            raise ValueError("Wrong value of the record: " + "".join(row) + "  Should be a number")
        except TypeError as error:
            raise TypeError("Wrong type of the record: " + "".join(row) + "  Should be a string")
        data.append(value)
    return data

def open_and_write_csv(filename, data):
    """
    Takes array of tuples (value in meters, value in feet)
    Writes csv file at filename
    """
    try:
        csv_file = open(filename,"w")
    except FileExistsError as er:
        raise FileExistsError("File with name" + filename + "already exists." )
    except FileNotFoundError as er:
        raise FileNotFoundError("Path " + filename + " not found. Please check the path you provided. ")
    except PermissionError as er:
        raise PermissionError("Cannot create file" + filename + ", permission denied. Error: {er}")


    fieldnames = ["Meters", "Feet" ]

    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for meters, feet  in data:
        csv_writer.writerow({'Meters': meters,'Feet':feet})

    csv_file.close()

def meters_to_inches(meters):
    """
    Takes array of values in meters
    Returns array of tuples (meters, inches)
    """

    result = []
    for value in meters:
        result.append((value, value*CONV_CEFFICIENT))
    return result



def converter(source_file, target_file):

    input_data = open_and_read_csv(source_file)
    output_data = meters_to_inches(input_data)
    open_and_write_csv(target_file, output_data)

if __name__ == "__main__":
    converter("/Users/leonidastrin/myrepo/csv/test.csv","/Users/leonidastrin/myrepo/csv/test2.csv")
#    converter("/User/leonidastrin/test.csv", "/User/leonidastrin/myrepo/csv/test2.csv")