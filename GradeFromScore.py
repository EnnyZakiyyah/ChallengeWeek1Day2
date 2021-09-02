print("Grade From Score".center(75, "="))
while True:
    nilai = int(input("Input Nilai 0 - 100 : "))
    if nilai >= 86 and nilai <= 100:
        hasil = "Grade A"
    elif nilai >= 75 and nilai <= 85:
        hasil = "Grade B"
    elif nilai >= 60 and nilai <= 74:
        hasil = "Grade C"
    elif nilai >= 50 and nilai <= 59:
        hasil = "Grade D"
    elif nilai >= 40 and nilai <= 49:
        hasil = "Grade E"
    elif nilai >= 0 and nilai <= 39:
        hasil = "Grade F"
    else:
        hasil = "Silahkan Input Kembali"

    print(f"Nilai {nilai}    : {hasil}")
