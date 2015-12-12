
def wrapping_paper_area_from_dimensions(dimensions):
    (l, w, h) = dimensions
    sides = [l * w, l * h, w * h]
    area_needed = 2 * sides[0] + 2 * sides[1] + 2 * sides[2] + min(sides)
    return area_needed

def ribbon_length_from_dimensions(dimensions):
    (l, w, h) = dimensions
    perimeters = [l + l + w + w, l + l + h + h, w + w + h + h]
    ribbon_length = min(perimeters)
    bow_length  = l * w * h
    return ribbon_length + bow_length

def load_input_dimensions():
    with open('data/day02_input.txt') as input_file:
        lines = input_file.readlines()
        for line in lines:
            dimensions = tuple([int(_) for _ in line.split('x')])
            yield dimensions

if __name__ == '__main__':
    input_dimensions = list(load_input_dimensions())

    total_wrapping_area = 0
    for dimensions in input_dimensions:
        total_wrapping_area += wrapping_paper_area_from_dimensions(dimensions)
    print 'Total wrapping paper needed: {0} sqft.'.format(total_wrapping_area)

    total_ribbon_length = 0
    for dimensions in input_dimensions:
        total_ribbon_length += ribbon_length_from_dimensions(dimensions)
    print 'Total ribbon needed: {0} ft.'.format(total_ribbon_length)

