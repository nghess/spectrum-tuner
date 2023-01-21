import re
import numpy as np
import matplotlib.pyplot as plt

# Import text file
txt = list(open('E:\spectrum-tuner\spectrum_demo.txt', 'r'))
# Trim first and last quotation marks from list to make indexable
txt = txt[0][1:-1]

# Find opening and closing braces.
lbrace_idx = [idx for idx, s in enumerate(txt) if '[' in s]
rbrace_idx = [idx for idx, s in enumerate(txt) if ']' in s]

# Slice list between spectrum points
spectrum_pts = txt[lbrace_idx[1]+1:rbrace_idx[0]]
# Flatten list to string, then split into new list using commas
spectrum_pts = str(spectrum_pts)
spectrum_pts = spectrum_pts.split(",")

# Remove dictionary notation
spectrum_pts = [x.replace(':', '') for x in spectrum_pts]
spectrum_pts = [x.replace('{', '') for x in spectrum_pts]
spectrum_pts = [x.replace('}', '') for x in spectrum_pts]
spectrum_pts = [x.replace(re.search(r'"(\d)+"', x)[0], "") for x in spectrum_pts]

# Convert list items to float
spectrum_pts = [float(x) for x in spectrum_pts]

# Build x-axis between 380-780 nm
wavelength = np.linspace(380, 780, 401)

# Visualize spectrum
plt.plot(wavelength, spectrum_pts)
plt.show() 