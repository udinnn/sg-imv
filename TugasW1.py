from tkinter import *
from tkinter import messagebox

# fungsi buat tombol reset
def reset():
    umurFrame.delete(0,'end')
    tinggiFrame.delete(0,'end')
    beratFrame.delete(0,'end')

"""
1. Cara Menghitung IMT Bayi Usia 1-6 Bulan
Rumusnya: Berat Badan Lahir (gr) + (Usia x 600 gram)

2. Cara Menghitung IMT Bayi Usia 7-12 Bulan
Rumusnya: Berat Badan Lahir (gr) + (Usia x 500 gram)

3. Cara Menghitung IMT Anak Usia 1-5 Tahun
Rumusnya: 2n + 8

4. Cara Menghitung IMT Dewasa
Rumusnya: Berat Badan (kg) : (Tinggi Badan (m) x Tinggi Badan (m))

https://health.detik.com/berita-detikhealth/d-4596983/5-cara-menghitung-imt-untuk-panduan-hidup-sehat """

# fungsi buat satuan metrik

def metric():
    tinggi = float(tinggiFrame.get())
    tinggi2 = tinggi/100
    berat = float(beratFrame.get())
    umur = float(umurFrame.get())

    # untuk umur bayi gramnya diconvert ke kg dlu

    if umur >= 0.1 and umur <= 0.6:
        BMI = berat + umur * 0.6
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    elif umur >= 0.7 and umur < 1:
        BMI =  berat + umur * 0.5
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    elif umur >= 1 and umur < 5:
        BMI =  2 * umur + 8
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    else:
        BMI =  berat / (tinggi2**2)
        hasilMetric(BMI)

# fungsi buat satuan imperial

def imperial():
    tinggi_inch  = float(tinggiFrame.get())
    tinggi_inch2 = tinggi_inch*0.0254
    berat_pound  = float(beratFrame.get())
    berat_pound2 = berat_pound*0.453592
    umur = float(umurFrame.get())

    # untuk umur bayi gramnya diconvert ke kg dlu

    if umur >= 0.1 and umur <= 0.6:
        BMI =  berat_pound2 + umur * 0.6
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    elif umur >= 0.7 and umur < 1:
        BMI =  berat_pound2 + umur * 0.5
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    elif umur >= 1 and umur < 5:
        BMI =  2 * umur + 8
        messagebox.showinfo('Hasil BMI', f"BMI anda: {BMI}")
    else:
        BMI =  berat_pound2 / (tinggi_inch2**2)
        hasilImperial(BMI)

def hasilMetric(BMI):
    BMI = round(BMI, 1)

    if BMI < 18.5:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI} termasuk kategori kurus")
    elif BMI > 18.5 and BMI < 22.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI} termasuk kategori normal")
    elif BMI > 23 and BMI < 24.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI} termasuk kategori kelebihan berat badan")
    elif BMI > 25 and BMI <29.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI} termasuk kategori obesitas")
    else:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI} termasuk kategori obesitas II")

def hasilImperial(BMI):
    BMI_ROUND = round(BMI, 1)

    if BMI_ROUND < 18.5:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI_ROUND} termasuk kategori kurus")
    elif BMI_ROUND > 18.5 and BMI_ROUND < 22.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI_ROUND} termasuk kategori normal")
    elif BMI_ROUND > 23 and BMI_ROUND < 24.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI_ROUND} termasuk kategori kelebihan berat badan")
    elif BMI_ROUND > 25 and BMI_ROUND <29.9:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI_ROUND} termasuk kategori obesitas")
    else:
        messagebox.showinfo('Hasil BMI', f"BMI anda {BMI_ROUND} termasuk kategori obesitas II")

# fungsi buat tombol ganti unit

def gantiUnit():
    if switchButton.config('text')[-1] == 'Ubah ke Imperial':
        tinggiLabel.config(text="Tinggi anda (inch): ")
        beratLabel.config(text="Berat anda (pound): ")
        tmblHitung.config(command=imperial)
        switchButton.config(text='Ubah ke Metric')
    else:
        tinggiLabel.config(text="Tinggi anda (cm): ")
        beratLabel.config(text="Berat anda (kg): ")
        tmblHitung.config(command=metric)
        switchButton.config(text='Ubah ke Imperial')

# Windows GUI Kalkulator
# referensi https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

windows = Tk()
windows.title('Kalkulator BMI')
windows.geometry('500x400')
windows.config(bg='Navy')

var = IntVar()

# Frame yg warna abu dibelakang label nama berat dll, pady sama padx itu panjang sama lebarnya terhadap ukuran windows geometry

frame = Frame(windows, padx=50, pady=50)
frame.pack(expand=True)

# button buat ganti mode 

switchButton = Button(frame, text="Ubah ke Imperial", command=gantiUnit)
switchButton.grid(row=1, columnspan=3, pady=10)

# button buat label tulisan umur sama kotak input umur

umurLabel = Label(frame, text="Umur anda: ")
umurLabel.grid(row=2, column=1)

umurFrame = Entry(frame)
umurFrame.grid(row=2, column=2, pady=5)

# button buat label tulisan tinggi sama kotak input tinggi

tinggiLabel = Label(frame, text="Tinggi anda (cm): ")
tinggiLabel.grid(row=3, column=1)

tinggiFrame = Entry(frame)
tinggiFrame.grid(row=3, column=2, pady=5)

# button buat label tulisan berat sama kotak input berat

beratLabel = Label(frame, text="Berat anda (kg): ")
beratLabel.grid(row=4, column=1)

beratFrame = Entry(frame)
beratFrame.grid(row=4, column=2, pady=5)

# 'frame' baru buat naro 3 button dibawah, sebenernya bisa aja gak pake tapi gak rapi jadinya

frame2 = Frame(frame)
frame2.grid(row=5, columnspan=3, pady=10)

# button yang kalo dipencet bakal ngambil nilai dari kolom teks dan ekseksi fungsi metrik secara default 

tmblHitung = Button(frame2, text='Hitung', command=metric)
tmblHitung.pack(side=LEFT)

# button yang kalo dipencet bakal ngehapus semua nilai dari kolom teks

tmblReset = Button(frame2, text='Reset', command=reset)
tmblReset.pack(side=LEFT)

# self explanatory

tmblExit = Button(frame2, text='Keluar', command=lambda:windows.destroy())
tmblExit.pack(side=RIGHT)

# mainloop dipake buat jalanin GUI nya

windows.mainloop()