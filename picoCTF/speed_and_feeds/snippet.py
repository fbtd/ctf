from PIL import Image
import numpy
import re


def str_to_coordinate(s):
    f = float(s)
    return int(f * 10)


def line_to_coordinates(line):
    '''returns a coordinate tuple or None if the line is invalid'''
    match = re.search(r'X(\d+\.\d{4})Y(-?\d+\.\d{4})', line)
    if match is None:
        return None
    coordinates = (str_to_coordinate(match[1]),
                   str_to_coordinate(match[2]) + 30)
    return coordinates


def main():
    data = numpy.zeros((2000, 100), dtype=numpy.uint8)

    with open('instructions', 'r') as f:
        for line in f:
            cooridnates = line_to_coordinates(line)
            if cooridnates == None:
                continue
            data[cooridnates] = 255
            print(cooridnates)
    image = Image.fromarray(data)
    image.save('cnc.png')

main()

# G1X196.5517Y-1.9310
# X: 0...200
# Y: -2...10