#!/usr/bin/env python
# encoding: utf-8

name = "Pt_fcc100_gemnet"
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
            NASAPolynomial(coeffs=[-0.0864099,0.0130134,-2.29934e-05,1.89209e-08,-5.94972e-12,2028.62,-0.449254], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.89836,-0.000365424,6.90274e-07,-3.922e-10,7.37923e-14,1462.3,-14.5985], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[-0.219089,0.0253731,-3.32871e-05,2.42281e-08,-7.08432e-12,-2959.09,0.919642], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.98859,-0.00707234,1.25325e-05,-6.61166e-09,1.17362e-12,-5158.88,-44.9337], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[3.28453,0.00623726,-8.63508e-06,7.00551e-09,-2.35776e-12,-34133.3,-14.4294], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.52486,-0.00150713,2.75487e-06,-1.51657e-09,2.78437e-13,-34694.8,-25.6739], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[-1.09987,0.0111682,-1.32947e-05,7.57243e-09,-1.67051e-12,-4861.27,4.16981], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.66995,-0.00126686,2.34233e-06,-1.31536e-09,2.45496e-13,-5787.16,-14.7711], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[4.46517,0.00265521,-5.3514e-06,4.83897e-09,-1.53528e-12,-1672.76,-17.3649], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.07305,-0.000633302,9.14037e-07,-3.14515e-10,3.34022e-14,-1750.23,-20.0826], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[0.204342,0.0116702,-2.04845e-05,1.67801e-08,-5.25948e-12,9156.49,-1.44076], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.90491,-0.000344088,6.49102e-07,-3.68593e-10,6.9325e-14,8639.94,-14.2641], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[0.871442,0.00937605,-1.70733e-05,1.43551e-08,-4.58628e-12,-17125.8,-4.30807], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93813,-0.000213064,4.05368e-07,-2.30906e-10,4.35086e-14,-17503.6,-14.0299], Tmin=(1000,'K'), Tmax=(2000,'K')),
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
            NASAPolynomial(coeffs=[0.448611,0.0191337,-3.42532e-05,2.88459e-08,-9.15974e-12,-26289.4,-3.29169], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.006,-0.00164318,2.82441e-06,-1.41161e-09,2.39618e-13,-27133,-24.799], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

