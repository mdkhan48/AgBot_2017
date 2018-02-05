detected = False

for detect_face in [90,90,90,110,110,110,90,90,90]:
    print(detect_face)
    if 80 < detect_face < 100:
        if detected:
            pass
        else:
            print(' 1')
            detected = True
    else:
        if detected:
            print(' 2')
            detected = False
        else:
            pass