import os
import glob
import pandas as pd

def run():
    extension = 'csv'
    
    os.chdir("csv/prod/")
    all_filenames = [os.path.splitext(i)[0] for i in glob.glob('*.{}'.format(extension))]

    fout=open("../final/combined_csv.csv","a",encoding="utf-8",errors="ignore")
    
    for filename in all_filenames:
        f = open(filename+'.csv',encoding="utf-8")
        for line in f:            
            new_line = '"'+filename+'",'+line
            fout.write(new_line)
    fout.close()

    #for f in all_filenames:
     #   f = open(f,encoding="utf-8")
      #  for line in f:
       #      fout.write(line)
        #f.close() # not really needed
    #fout.close()

if __name__ == "__main__":
    run()