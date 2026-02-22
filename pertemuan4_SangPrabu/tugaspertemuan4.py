while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        hasil = angka1 / angka2
        
    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError:
        print("Error: Tidak boleh membagi dengan nol!")
    else:
        print("Hasil pembagian:", hasil)
        break
    finally:
        print("Percobaan selesai.\n")