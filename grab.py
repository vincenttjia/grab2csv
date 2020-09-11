import subprocess
import sys
from os import listdir
from os.path import isfile

input_path = "./input/"
output_file = "./grab.csv"

def convert_tanggal(tanggal):
	return tanggal.replace("Januari","January").replace("Febuari","February").replace("Maret","March").replace("April","April").replace("Mei","May").replace("Juni","June").replace("Juli","July").replace("Agustus","August").replace("September","September").replace("Oktober","October").replace("November","November").replace("Desember","December")

def get_csv(pdf):
	output = subprocess.Popen(["pdftotext", pdf, "-"], stdout=subprocess.PIPE).communicate()[0]
	outputs = output.decode("utf-8") 
	array = outputs.split("\r\n")
	string = convert_tanggal(array[1].split(",")[0])+","+array[5]+","+array[15].split(" ")[0]+","+array[29].replace(".","").replace(",",".")+","+array[31].replace(".","").replace(",",".")+","+array[33].replace(".","").replace(",",".")+","+array[35].replace(".","").replace(",",".")+","+array[37].replace(".","").replace(",",".")+","+array[41].replace(".","").replace(",",".")+"\n"
	return string

def main():
	global input_path,output_file
	if(isfile(output_file)):
		while(True):
			selection = input(output_file+" ada apakah anda ingin lanjut(Y/N)")
			selection = selection.upper()
			if(selection=="Y"):
				break
			elif(selection=="N"):
				sys.exit(0)

	f = open(output_file,"w+")
	f.write("Tanggal,Nama,Total Pesanan,Nilai Pesanan,PB1,Promosi yang Dibiayai Merchant,Komisi & Pajak,Diskon Ongkir,Total Pendapatan\n")
	files = listdir(input_path)
	
	for file in files:
		path = input_path+file
		string = get_csv(path)
		f.write(string)

	

if __name__ == "__main__":
	main()