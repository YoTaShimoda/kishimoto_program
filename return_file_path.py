import glob
import read_file

numfour = glob.glob('/Users/yota/csv_marge/no4-1/*')
numfive = glob.glob('/Users/yota/csv_marge/no5-1/*')
hertfour = glob.glob('/Users/yota/csv_marge/心拍4/*')
hertfive = glob.glob('/Users/yota/csv_marge/心拍5/*')


numfour = sorted(numfour)
numfive = sorted(numfive)
hertfour = sorted(hertfour)
hertfive = sorted(hertfive)

for i in range(0,len(hertfour)):
    read_file.read_and_write_file(hertfour[i], numfour[i])