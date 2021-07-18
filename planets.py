import math
import micropython

planets_a = micropython.const([
    [bytes([
        47, 49, 110, 110, 110,
        47, 50, 73, 73, 73,
        47, 51, 73, 73, 73,
        48, 48, 125, 125, 125,
        48, 49, 110, 110, 110,
        48, 50, 133, 131, 130,
        48, 51, 117, 117, 116,
        48, 52, 110, 110, 110,
        49, 47, 73, 73, 73,
        49, 48, 108, 107, 106,
        49, 49, 110, 110, 110,
        49, 50, 197, 192, 192,
        49, 51, 159, 157, 157,
        49, 52, 110, 110, 110,
        49, 53, 73, 73, 73,
        50, 47, 73, 73, 73,
        50, 48, 111, 106, 100,
        50, 49, 152, 124, 92,
        50, 50, 111, 106, 100,
        50, 51, 110, 110, 110,
        50, 52, 111, 106, 100,
        50, 53, 73, 73, 73,
        51, 47, 73, 73, 73,
        51, 48, 111, 106, 100,
        51, 49, 111, 106, 100,
        51, 50, 152, 124, 92,
        51, 51, 64, 64, 64,
        51, 52, 111, 106, 100,
        51, 53, 110, 110, 110,
        52, 48, 73, 73, 73,
        52, 49, 64, 64, 64,
        52, 50, 73, 73, 73,
        52, 51, 111, 106, 100,
        52, 52, 110, 110, 110,
        53, 49, 73, 73, 73,
        53, 50, 64, 64, 64,
        53, 51, 110, 110, 110,
    ])],
    [bytes([
        47, 49, 152, 126, 105,
        47, 50, 172, 137, 108,
        47, 51, 209, 153, 108,
        48, 48, 204, 172, 146,
        48, 49, 172, 137, 108,
        48, 50, 185, 125, 76,
        48, 51, 204, 172, 146,
        48, 52, 239, 172, 40,
        49, 47, 204, 172, 146,
        49, 48, 172, 137, 108,
        49, 49, 185, 125, 76,
        49, 50, 170, 117, 73,
        49, 51, 157, 128, 104,
        49, 52, 204, 172, 146,
        49, 53, 204, 172, 146,
        50, 47, 185, 125, 76,
        50, 48, 209, 153, 108,
        50, 49, 239, 172, 40,
        50, 50, 157, 128, 104,
        50, 51, 204, 172, 146,
        50, 52, 209, 153, 108,
        50, 53, 197, 192, 192,
        51, 47, 185, 125, 76,
        51, 48, 172, 137, 108,
        51, 49, 157, 128, 104,
        51, 50, 204, 172, 146,
        51, 51, 209, 153, 108,
        51, 52, 197, 192, 192,
        51, 53, 207, 184, 164,
        52, 48, 209, 153, 108,
        52, 49, 204, 172, 146,
        52, 50, 204, 172, 146,
        52, 51, 197, 192, 192,
        52, 52, 211, 211, 211,
        53, 49, 192, 148, 60,
        53, 50, 209, 153, 108,
        53, 51, 211, 211, 211,
    ])],
    [bytes([
        47, 49, 60, 159, 156,
        47, 50, 37, 189, 37,
        47, 51, 37, 189, 122,
        48, 48, 37, 189, 122,
        48, 49, 37, 189, 37,
        48, 50, 37, 189, 37,
        48, 51, 37, 189, 122,
        48, 52, 50, 134, 131,
        49, 47, 60, 159, 156,
        49, 48, 37, 189, 37,
        49, 49, 28, 99, 28,
        49, 50, 37, 189, 122,
        49, 51, 37, 189, 37,
        49, 52, 60, 159, 156,
        49, 53, 201, 201, 201,
        50, 47, 228, 228, 228,
        50, 48, 37, 189, 122,
        50, 49, 60, 159, 156,
        50, 50, 71, 188, 184,
        50, 51, 60, 159, 156,
        50, 52, 60, 159, 156,
        50, 53, 190, 190, 190,
        51, 47, 206, 206, 206,
        51, 48, 39, 153, 39,
        51, 49, 39, 153, 39,
        51, 50, 38, 132, 38,
        51, 51, 37, 189, 37,
        51, 52, 37, 189, 37,
        51, 53, 100, 175, 172,
        52, 48, 60, 159, 156,
        52, 49, 60, 159, 156,
        52, 50, 38, 132, 38,
        52, 51, 37, 189, 37,
        52, 52, 60, 159, 156,
        53, 49, 71, 169, 165,
        53, 50, 60, 159, 156,
        53, 51, 49, 135, 132,
    ])],
    [bytes([
        47, 49, 168, 56, 41,
        47, 50, 155, 26, 10,
        47, 51, 182, 54, 37,
        48, 48, 190, 74, 59,
        48, 49, 155, 26, 10,
        48, 50, 182, 54, 37,
        48, 51, 155, 26, 10,
        48, 52, 171, 55, 40,
        49, 47, 155, 26, 10,
        49, 48, 139, 31, 17,
        49, 49, 155, 26, 10,
        49, 50, 195, 108, 97,
        49, 51, 192, 87, 73,
        49, 52, 155, 26, 10,
        49, 53, 190, 74, 59,
        50, 47, 90, 20, 10,
        50, 48, 111, 27, 14,
        50, 49, 155, 26, 10,
        50, 50, 155, 26, 10,
        50, 51, 155, 26, 10,
        50, 52, 130, 29, 16,
        50, 53, 155, 26, 10,
        51, 47, 65, 15, 8,
        51, 48, 155, 26, 10,
        51, 49, 119, 25, 11,
        51, 50, 155, 26, 10,
        51, 51, 107, 25, 13,
        51, 52, 90, 20, 10,
        51, 53, 111, 27, 14,
        52, 48, 65, 15, 8,
        52, 49, 90, 20, 10,
        52, 50, 155, 26, 10,
        52, 51, 90, 20, 10,
        52, 52, 111, 27, 14,
        53, 49, 155, 26, 10,
        53, 50, 130, 27, 13,
        53, 51, 155, 26, 10,
    ])],
    [bytes([
        47, 49, 190, 165, 137,
        47, 50, 239, 183, 117,
        47, 51, 190, 165, 137,
        48, 48, 190, 165, 137,
        48, 49, 216, 175, 129,
        48, 50, 197, 192, 192,
        48, 51, 233, 146, 109,
        48, 52, 239, 183, 117,
        49, 47, 239, 183, 117,
        49, 48, 216, 175, 129,
        49, 49, 197, 192, 192,
        49, 50, 208, 127, 92,
        49, 51, 184, 153, 118,
        49, 52, 216, 175, 129,
        49, 53, 194, 188, 174,
        50, 47, 239, 183, 117,
        50, 48, 190, 165, 137,
        50, 49, 216, 175, 129,
        50, 50, 233, 146, 109,
        50, 51, 208, 127, 92,
        50, 52, 197, 192, 192,
        50, 53, 167, 173, 192,
        51, 47, 216, 175, 129,
        51, 48, 197, 192, 192,
        51, 49, 233, 146, 109,
        51, 50, 137, 70, 52,
        51, 51, 119, 52, 33,
        51, 52, 197, 192, 192,
        51, 53, 143, 149, 166,
        52, 48, 239, 183, 117,
        52, 49, 197, 192, 192,
        52, 50, 216, 175, 129,
        52, 51, 216, 175, 129,
        52, 52, 239, 183, 117,
        53, 49, 239, 183, 117,
        53, 50, 239, 183, 117,
        53, 51, 209, 158, 99,
    ])],
    [bytes([
        46, 50, 233, 233, 233,
        47, 49, 191, 183, 94,
        47, 50, 191, 183, 94,
        47, 51, 233, 233, 233,
        48, 48, 176, 171, 114,
        48, 49, 191, 183, 94,
        48, 50, 191, 183, 94,
        48, 51, 233, 233, 233,
        48, 52, 226, 216, 110,
        49, 47, 176, 171, 114,
        49, 48, 176, 171, 114,
        49, 49, 191, 183, 94,
        49, 50, 226, 216, 110,
        49, 51, 233, 233, 233,
        49, 52, 226, 216, 110,
        49, 53, 211, 202, 98,
        50, 47, 176, 171, 114,
        50, 48, 191, 183, 94,
        50, 49, 191, 183, 94,
        50, 50, 226, 216, 110,
        50, 51, 233, 233, 233,
        50, 52, 226, 216, 110,
        50, 53, 211, 202, 98,
        51, 47, 191, 183, 94,
        51, 48, 191, 183, 94,
        51, 49, 191, 183, 94,
        51, 50, 226, 216, 110,
        51, 51, 233, 233, 233,
        51, 52, 211, 202, 98,
        51, 53, 211, 202, 98,
        52, 48, 191, 183, 94,
        52, 49, 226, 216, 110,
        52, 50, 226, 216, 110,
        52, 51, 233, 233, 233,
        52, 52, 211, 202, 98,
        53, 49, 226, 216, 110,
        53, 50, 226, 216, 110,
        53, 51, 233, 233, 233,
        54, 50, 233, 233, 233,
    ])],
    [bytes([
        47, 49, 104, 222, 240,
        47, 50, 92, 203, 220,
        47, 51, 92, 203, 220,
        48, 48, 104, 222, 240,
        48, 49, 104, 222, 240,
        48, 50, 92, 203, 220,
        48, 51, 92, 203, 220,
        48, 52, 92, 203, 220,
        49, 47, 104, 222, 240,
        49, 48, 104, 222, 240,
        49, 49, 92, 203, 220,
        49, 50, 92, 203, 220,
        49, 51, 92, 203, 220,
        49, 52, 92, 203, 220,
        49, 53, 92, 203, 220,
        50, 47, 92, 203, 220,
        50, 48, 92, 203, 220,
        50, 49, 92, 203, 220,
        50, 50, 92, 203, 220,
        50, 51, 92, 203, 220,
        50, 52, 92, 203, 220,
        50, 53, 92, 203, 220,
        51, 47, 92, 203, 220,
        51, 48, 92, 203, 220,
        51, 49, 92, 203, 220,
        51, 50, 92, 203, 220,
        51, 51, 92, 203, 220,
        51, 52, 75, 176, 192,
        51, 53, 75, 176, 192,
        52, 48, 92, 203, 220,
        52, 49, 92, 203, 220,
        52, 50, 92, 203, 220,
        52, 51, 75, 176, 192,
        52, 52, 75, 176, 192,
        53, 49, 92, 203, 220,
        53, 50, 75, 176, 192,
        53, 51, 75, 176, 192,
    ])],
    [bytes([
        47, 49, 37, 69, 225,
        47, 50, 37, 69, 225,
        47, 51, 28, 61, 224,
        48, 48, 37, 69, 225,
        48, 49, 28, 61, 224,
        48, 50, 28, 61, 224,
        48, 51, 28, 61, 224,
        48, 52, 28, 61, 224,
        49, 47, 37, 69, 225,
        49, 48, 28, 61, 224,
        49, 49, 82, 104, 215,
        49, 50, 28, 61, 224,
        49, 51, 28, 61, 224,
        49, 52, 30, 58, 199,
        49, 53, 37, 64, 200,
        50, 47, 28, 61, 224,
        50, 48, 28, 61, 224,
        50, 49, 101, 122, 224,
        50, 50, 28, 61, 224,
        50, 51, 28, 61, 224,
        50, 52, 30, 58, 199,
        50, 53, 28, 52, 168,
        51, 47, 28, 61, 224,
        51, 48, 28, 61, 224,
        51, 49, 28, 61, 224,
        51, 50, 28, 61, 224,
        51, 51, 30, 58, 199,
        51, 52, 30, 58, 199,
        51, 53, 28, 52, 168,
        52, 48, 28, 59, 215,
        52, 49, 25, 55, 203,
        52, 50, 30, 58, 199,
        52, 51, 30, 58, 199,
        52, 52, 28, 52, 168,
        53, 49, 28, 59, 215,
        53, 50, 28, 52, 168,
        53, 51, 28, 52, 168,
    ])],
])


def coordinates(year, month, day, hour, minute):
    jdn = ((367 * year - math.floor(7 * (year + math.floor((month + 9) / 12)) / 4)) + math.floor(275 * month / 9) +
           (day + 1721013.5))
    jd = (jdn + hour / 24. + minute / 1440.)
    d = jd - 2451543.5

    w = 282.9404 + 4.70935E-5 * d
    e = (0.016709 - (1.151E-9 * d))
    m2 = normalize(356.047 + 0.9856002585 * d)

    m = math.radians(m2)
    e_capt = m2 + (180 / math.pi) * e * math.sin(m) * (1 + e * math.cos(m))
    e_capt = math.radians(e_capt)
    x = math.cos(e_capt) - e
    y = math.sin(e_capt) * math.sqrt(1 - e * e)

    r = math.sqrt(x * x + y * y)

    v = math.atan2(y, x)
    v = math.degrees(v)
    lon = (v + w)
    lon = normalize(lon)
    lon = math.radians(lon)
    x2 = r * math.cos(lon)
    y2 = r * math.sin(lon)

    earthX = -1 * x2
    earthY = -1 * y2
    earthZ = 0

    n_er = 48.3313 + 3.24587E-5 * d
    i_er = 7.0047 + 5.00E-8 * d
    w_er = 29.1241 + 1.01444E-5 * d
    a_er = 0.387098
    e_er = 0.205635 + 5.59E-10 * d
    m_er = 168.6562 + 4.0923344368 * d

    m_er = normalize(m_er)

    n_af = 76.6799 + 2.46590E-5 * d
    i_af = 3.3946 + 2.75E-8 * d
    w_af = 54.8910 + 1.38374E-5 * d
    a_af = 0.723330
    e_af = 0.006773 - 1.30E-9 * d
    m_af = 48.0052 + 1.6021302244 * d

    m_af = normalize(m_af)

    n_ar = 49.5574 + 2.11081E-5 * d
    i_ar = 1.8497 - 1.78E-8 * d
    w_ar = 286.5016 + 2.92961E-5 * d
    a_ar = 1.523688
    e_ar = 0.093405 + 2.51E-9 * d
    m_ar = 18.6021 + 0.5240207766 * d

    m_ar = normalize(m_ar)

    n_di = 100.4542 + 2.76854E-5 * d
    i_di = 1.3030 - 1.557E-7 * d
    w_di = 273.8777 + 1.6450E-5 * d
    a_di = 5.20256
    e_di = 0.048498 + 4.469E-9 * d
    m_di = 19.8950 + 0.0830853001 * d

    m_di = normalize(m_di)

    n_kr = 113.6634 + 2.38980E-5 * d
    i_kr = 2.4886 - 1.081E-7 * d
    w_kr = 339.3939 + 2.97661E-5 * d
    a_kr = 9.55475
    e_kr = 0.055546 - 9.499E-9 * d
    m_kr = 316.9670 + 0.0334442282 * d

    m_kr = normalize(m_kr)

    n_ou = 74.0005 + 1.3978E-5 * d
    i_ou = 0.7733 + 1.9E-8 * d
    w_ou = 96.6612 + 3.0565E-5 * d
    a_ou = 19.18171 - 1.55E-8 * d
    e_ou = 0.047318 + 7.45E-9 * d
    m_ou = 142.5905 + 0.011725806 * d

    m_ou = normalize(m_ou)

    n_po = 131.7806 + 3.0173E-5 * d
    i_po = 1.7700 - 2.55E-7 * d
    w_po = 272.8461 - 6.027E-6 * d
    a_po = 30.05826 + 3.313E-8 * d
    e_po = 0.008606 + 2.15E-9 * d
    m_po = 260.2471 + 0.005995147 * d

    m_po = normalize(m_po)
    xereclip, yereclip, zereclip, long2_er, lat2_er, r_er = from_sun(m_er,
                                                               e_er, a_er, n_er, w_er, i_er)
    xafeclip, yafeclip, zafeclip, long2_af, lat2_af, r_af = from_sun(m_af,
                                                                     e_af, a_af, n_af, w_af, i_af)
    xareclip, yareclip, zareclip, long2_ar, lat2_ar, r_ar = from_sun(m_ar,
                                                                     e_ar, a_ar, n_ar, w_ar, i_ar)
    xdieclip, ydieclip, zdieclip, long2_di, lat2_di, r_di = from_sun(m_di,
                                                                     e_di, a_di, n_di, w_di, i_di)
    xkreclip, ykreclip, zkreclip, long2_kr, lat2_kr, r_kr = from_sun(m_kr,
                                                                     e_kr, a_kr, n_kr, w_kr, i_kr)
    xoueclip, youeclip, zoueclip, long2_ou, lat2_ou, r_ou = from_sun(m_ou,
                                                                     e_ou, a_ou, n_ou, w_ou, i_ou)
    xpoeclip, ypoeclip, zpoeclip, long2_po, lat2_po, r_po = from_sun(m_po,
                                                                     e_po, a_po, n_po, w_po, i_po)
    m_di = normalize(m_di)
    m_kr = normalize(m_kr)
    m_ou = normalize(m_ou)

    di_diat1 = -0.332 * math.sin(math.radians(2 * m_di - 5 * m_kr - 67.6))
    di_diat2 = -0.056 * math.sin(math.radians(2 * m_di - 2 * m_kr + 21))
    di_diat3 = 0.042 * math.sin(math.radians(3 * m_di - 5 * m_kr + 21))
    di_diat4 = -0.036 * math.sin(math.radians(m_di - 2 * m_kr))
    di_diat5 = 0.022 * math.cos(math.radians(m_di - m_kr))
    di_diat6 = 0.023 * math.sin(math.radians(2 * m_di - 3 * m_kr + 52))
    di_diat7 = -0.016 * math.sin(math.radians(m_di - 5 * m_kr - 69))

    kr_diat1 = 0.812 * math.sin(math.radians(2 * m_di - 5 * m_kr - 67.6))
    kr_diat2 = -0.229 * math.cos(math.radians(2 * m_di - 4 * m_kr - 2))
    kr_diat3 = 0.119 * math.sin(math.radians(m_di - 2 * m_kr - 3))
    kr_diat4 = 0.046 * math.sin(math.radians(2 * m_di - 6 * m_kr - 69))
    kr_diat5 = 0.014 * math.sin(math.radians(m_di - 3 * m_kr + 32))

    kr_diat6 = -0.02 * math.cos(math.radians(2 * m_di - 4 * m_kr - 2))
    kr_diat7 = 0.018 * math.sin(math.radians(2 * m_di - 6 * m_kr - 49))

    ou_diat1 = 0.04 * math.sin(math.radians(m_kr - 2 * m_ou + 6))
    ou_diat2 = 0.035 * math.sin(math.radians(m_kr - 3 * m_ou + 33))
    ou_diat3 = -0.015 * math.sin(math.radians(m_di - m_ou + 20))

    diataraxes_long_di = (di_diat1 + di_diat2 + di_diat3 + di_diat4 +
                          di_diat5 + di_diat6 + di_diat7)
    diataraxes_long_kr = (kr_diat1 + kr_diat2 + kr_diat3 + kr_diat4
                          + kr_diat5)
    diataraxes_lat_kr = (kr_diat6 + kr_diat7)
    diataraxes_long_ou = (ou_diat1 + ou_diat2 + ou_diat3)

    long2_di = long2_di + diataraxes_long_di
    long2_kr = long2_kr + diataraxes_long_kr
    lat2_kr = lat2_kr + diataraxes_lat_kr
    long2_ou = long2_ou + diataraxes_long_ou

    long2_di = (math.radians(long2_di))
    lat2_di = (math.radians(lat2_di))
    long2_kr = (math.radians(long2_kr))
    lat2_kr = (math.radians(lat2_kr))
    long2_ou = (math.radians(long2_ou))
    lat2_ou = (math.radians(lat2_ou))

    xdieclip = r_di * math.cos(long2_di) * math.cos(lat2_di)
    ydieclip = r_di * math.sin(long2_di) * math.cos(lat2_di)
    zdieclip = r_di * math.sin(lat2_di)
    xkreclip = r_kr * math.cos(long2_kr) * math.cos(lat2_kr)
    ykreclip = r_kr * math.sin(long2_kr) * math.cos(lat2_kr)
    zkreclip = r_kr * math.sin(lat2_kr)
    xoueclip = r_ou * math.cos(long2_ou) * math.cos(lat2_ou)
    youeclip = r_ou * math.sin(long2_ou) * math.cos(lat2_ou)
    zoueclip = r_ou * math.sin(lat2_ou)

    return [(xereclip, yereclip, zereclip),  # Mercury
            (xafeclip, yafeclip, zafeclip),  # Venus
            (earthX, earthY, earthZ),        # Earth
            (xareclip, yareclip, zareclip),  # Mars
            (xdieclip, ydieclip, zdieclip),  # Jupiter
            (xkreclip, ykreclip, zkreclip),  # Saturn
            (xoueclip, youeclip, zoueclip),  # Uranus
            (xpoeclip, ypoeclip, zpoeclip)   # Neptune
            ]


def normalize(degrees):
    return degrees % 360


def from_sun(m, e, a, n, w, i):
    m2 = math.radians(m)
    e0 = m + (180 / math.pi) * e * math.sin(m2) * (1 + e * math.cos(m2))
    e0 = normalize(e0)
    e02 = math.radians(e0)
    e1 = normalize(e0 - (e0 - (180 / math.pi) * e * math.sin(e02) - m) / (1 - e * math.cos(e02)))
    e_capt = math.radians(e1)
    x = a * (math.cos(e_capt) - e)
    y = a * (math.sqrt(1 - e * e)) * math.sin(e_capt)

    r = math.sqrt(x * x + y * y)
    v = math.atan2(y, x)
    v = normalize(math.degrees(v))

    xeclip = r * (math.cos(math.radians(n)) * math.cos(math.radians(v + w)) - math.sin(math.radians(n)) * math.sin(
        math.radians(v + w)) * math.cos(math.radians(i)))
    yeclip = r * (math.sin(math.radians(n)) * math.cos(math.radians(v + w)) + math.cos(math.radians(n)) * math.sin(
        math.radians(v + w)) * math.cos(math.radians(i)))
    zeclip = r * math.sin(math.radians(v + w)) * math.sin(math.radians(i))
    long2 = math.atan2(yeclip, xeclip)
    long2 = normalize(math.degrees(long2))
    lat2 = math.atan2(zeclip, math.sqrt(xeclip * xeclip + yeclip * yeclip))
    lat2 = math.degrees(lat2)
    return (xeclip, yeclip, zeclip, long2, lat2, r)


