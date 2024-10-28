# ray_ellipsoid_intersection.py
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z

# find the intersection point (if it exists) between a ray and the Earth reference ellipsoid
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin

# Output:
#   shape and operation count of a convolution layer
#
# Written by Connor Walsh
# Other contributors: Brad Denby
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math
# "constants"
R_E = 6378.1363
e_E = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
d_l_x = float('nan') #: x-component of origin-referenced ray direction
d_l_y = float('nan') #: y-component of origin-referenced ray direction
d_l_z = float('nan') #: z-component of origin-referenced ray direction
c_l_x = float('nan') #: x-component offset of ray origin
c_l_y = float('nan') #: y-component offset of ray origin
c_l_z = float('nan') #: z-component offset of ray origin

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1]) #: x-component of origin-referenced ray direction
    d_l_y = float(sys.argv[2]) #: y-component of origin-referenced ray direction
    d_l_z = float(sys.argv[3]) #: z-component of origin-referenced ray direction
    c_l_x = float(sys.argv[4]) #: x-component offset of ray origin
    c_l_y = float(sys.argv[5]) #: y-component offset of ray origin
    c_l_z = float(sys.argv[6]) #: z-component offset of ray origin

else:
  print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

# write script below this line

a = d_l_x*d_l_x + d_l_y*d_l_y + d_l_z*d_l_z/(1 - e_E*e_E)
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + d_l_z*c_l_z/(1 - e_E*e_E))
c = c_l_x*c_l_x + c_l_y*c_l_y + c_l_z*c_l_z/(1 - e_E*e_E) - R_E*R_E

discr = b*b - 4.0*a*c
if discr>=0.0:
    d = (-b-math.sqrt(discr))/(2.0*a)
if d<0.0:
    d = (-b+math.sqrt(discr))/(2.0*a)


# d = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
l_d = [d*d_l_x + c_l_x, d*d_l_y + c_l_y, d*d_l_z + c_l_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point