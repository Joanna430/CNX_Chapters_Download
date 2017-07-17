import webbrowser
import csv
import os

def read_csv(csv_file_name):
    reader = csv.reader(open(csv_file_name), delimiter=',')
    url_list = []
    for row in reader:
        export_url = row[2] + "module_export?format=zip&export=Export"
        url_list.append(export_url)
    return url_list

"""
NOTICE:
Change the number in the following "range()" bracket in order to download the corresponding CNX chapters.
Index:
Preface -- range(0,1)
Units and Measurement -- range(1,9)
Vectors -- range(9,14)
Motion Along a Straight Line -- range(14,21)
Motion in Two and Three Dimensions -- range(21,27)
Newton's Laws of Motion -- range(27,35)
Applications of Newton's Laws -- range(35,40)
Work and Kinetic Energy -- range(40,45)
Potential Energy and Conservation of Energy -- range(45,51)
Linear Momentum and Collisions -- range(51,59)
Fixed-Axis Rotation -- range(59,68)
Angular Momentum -- range(68,73)
Static Equilibrium and Elasticity -- range(73,78)
Gravitation -- range(78,86)
Fluid Mechanics -- range(86,94)
Oscillations -- range(94,101)
Waves -- range(101,108)
Sound -- range(108,117)
Temperature and Heat -- range(117,124)
The Kinetic Theory of Gases -- range(124,129)
The First Law of Thermodynamics -- range(129,136)
The Second Law of Thermodynamics -- range(136,144)
Electric Charges and Fields -- range(144,152)
Gauss's Law -- range(152,157)
Electric Potential -- range(157,164)
Capacitance -- range(164,170)
Current and Resistance -- range(170,177)
Direct-Current Circuits -- range(177,184)
Magnetic Forces and Fields -- range(184,192)
Sources of Magnetic Fields -- range(192,200)
Electromagnetic Induction -- range(200,208)
Inductance -- range(208,215)
Alternating-Current Circuits -- range(215,222)
Electromagnetic Waves -- range(222,228)
The Nature of Light -- range(228,236)
Geometric Optics and Image Formation -- range(236,245)
Interference -- range(245,251)
Diffraction -- range(251,259)
Relativity -- range(259,269)
Photons and Matter Waves -- range(269,276)
Quantum Mechanics -- range(276,283)
Atomic Structure -- range(283,290)
Condensed Matter Physics -- range(290,299)
Nuclear Physics -- range(299,307)
Particle Physics and Cosmology -- range(307,315)
Appendices -- range(315,322)

For example, if you want to download Appendices, then the following code should be:
for idx in range(315,322):
  webbrowser.open(read_csv("oxup-legacy-links.csv")[idx])

The code will automatically open the download link and save to the download file in your computer.
"""
for idx in range(315,322):
  webbrowser.open(read_csv("oxup-legacy-links.csv")[idx])
