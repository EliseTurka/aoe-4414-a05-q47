# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  Determines the output shape and operation count of a convolution layer
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter weight count
# s: stride of convolution
# p: amount of padding on each of the four input map slides
#
# Output:
#  Prints the output channel count, output height count, putput width count, # of + 
#  performed, # of x performed, # of / performed
#
# Written by Elise Turka
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan')
n_filt = float('nan') 
h_filt = float('nan') 
w_filt = float('nan')
s = float('nan') 
p = float('nan')

# parse script arguments
if len(sys.argv)==9:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  n_filt = float(sys.argv[4])
  h_filt = float(sys.argv[5])
  w_filt = float(sys.argv[6])
  s = float(sys.argv[7])
  p = float(sys.argv[8])
else:
  print(\
   'Usage: '\
   ' python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
  )
  exit()


#calculating
h_out = (h_in+2*p-h_filt)/s+1
w_out = (w_in+2*p-w_filt)/s+1
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
c_out = n_filt
divs = 0


#printing output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))