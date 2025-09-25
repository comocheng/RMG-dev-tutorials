#!/usr/bin/env python
# encoding: utf-8

name = "Pt_fcc111_gemnet"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "X",
    molecule = 
"""
1 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0,0,0,0,0,0,0], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0,0,0,0,0,0,0], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "C_ads",
    molecule = 
"""
1 C u0 p0 c0 {2,Q}
2 X u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.962471,0.0164526,-2.87616e-05,2.34871e-08,-7.34397e-12,9544.02,2.85498], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86364,-0.000495635,9.34377e-07,-5.30479e-10,9.97619e-14,8809.01,-15.3297], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CH3_ads",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.274452,0.0248291,-3.16718e-05,2.25845e-08,-6.50416e-12,-1206.09,1.06374], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.94133,-0.00718686,1.27355e-05,-6.71966e-09,1.19297e-12,-3429.67,-44.9405], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "CO_ads",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69402,0.00432552,-4.73672e-06,3.42864e-09,-1.14361e-12,-31244,-16.1239], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.55966,-0.00142517,2.60618e-06,-1.43699e-09,2.64182e-13,-31747.1,-25.6621], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "H_ads",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15484,0.0147146,-2.29236e-05,1.72011e-08,-5.04873e-12,-4545.95,3.95892], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.78141,-0.000830122,1.54603e-06,-8.72259e-10,1.63346e-13,-5390.5,-15.2005], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "H2_ads",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.59243,0.00206258,-4.2361e-06,3.88277e-09,-1.22523e-12,-896.806,-16.786], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.07715,-0.000631491,9.09861e-07,-3.11931e-10,3.28531e-14,-952.759,-18.9295], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "N_ads",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 X u0 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0502796,0.0133687,-2.42602e-05,2.0348e-08,-6.48924e-12,6626.02,-1.17763], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.91005,-0.000311612,5.92289e-07,-3.37271e-10,6.35391e-14,6082.45,-15.1159], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "O_ads",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35812,0.00750767,-1.40123e-05,1.1985e-08,-3.87683e-12,-15479.7,-6.94493], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95752,-0.000138695,2.66212e-07,-1.52084e-10,2.87034e-14,-15762.2,-14.4167], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "OH_ads",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65972,0.0134556,-2.35061e-05,1.95515e-08,-6.1293e-12,-19127.2,-5.44069], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.02547,-0.00152636,2.5972e-06,-1.27927e-09,2.14398e-13,-19764.1,-21.4025], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

