import math
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * (1 + rate_per_period)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(500,.04,10,10)
1061.8348
1061.8348

print "=================="
print

def polygon_area(n, s):
    """returns the area of a polygon,
    with given n of sides and thier lengiths
    """
    return (n * s ** 2) /(4 * math.tan(math.pi/n))

print polygon_area(7, 3)
print polygon_area(5, 7)
print "============"

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
