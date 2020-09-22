vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu (M, m, N, n): ").capitalize()
treening = int(input("Sisestage enda vanus (1-tervisetreening, 2-põhivastupidavuse treening, 3-intensiivne aeroobne treening: "))

mmax = 220 - vanus
nmax = round(206 - (vanus * 0.88))

if treening == 1:
    mink = 0.50
    maxk = 0.70

if treening == 2:
    mink = 0.70
    maxk = 0.80

if treening == 3:
    mink = 0.80
    maxk = 0.87



if sugu == "N":
    nmin = round(nmax * mink)
    nmax = round(nmax * maxk)
    print("Pulsisagedus peaks olema vahemikus "+str(nmin)+" kuni "+str(nmax)+".")
elif sugu == "M":
    mmin = round(mmax * mink)
    mmax = round(mmax * maxk)
    print("Pulsisagedus peaks olema vahemikus " + str(mmin) + " kuni " + str(mmax) + ".")
