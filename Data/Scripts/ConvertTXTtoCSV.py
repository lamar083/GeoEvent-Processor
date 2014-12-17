
import csv
import glob
import os
import sys
import tempfile
import shutil

directory = " " #update with path to folder containing input GPS files from mobile device.
output = "C:/GeoEvent/Input" #local folder registered with GEP data store as the input folder.

txt_files = os.path.join(directory, '*.txt')

for txt_file in glob.glob(txt_files):
    
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        with open(txt_file) as finput:
            
            with open(tmp.name,'wb') as ftmp:
                writer = csv.writer(ftmp)
                for i, row in enumerate(csv.reader(finput)):
                    #to_append = "Filename" if i == 0 else txt_file
                    to_append = "Filename" if i == 0 else os.path.basename(txt_file)
                    writer.writerow(row+[to_append[0:8]])
        shutil.move(tmp.name,txt_file)
    except Exception, e:
        print >> sys.stderr, "does not exist"
        print >> sys.stderr, "Exception: %s" % str(e)
        #sys.exit(1)  
                
for txt_file in glob.glob(txt_files):
    if not os.path.isfile(txt_file):
        pass
    else:
        with open(txt_file, "rb") as input_file:
            in_txt = csv.reader(input_file, delimiter=',')
            next(in_txt, None)
            filename = os.path.splitext(os.path.basename(txt_file))[0] + '.csv'
            
            with open(os.path.join(output, filename), 'wb') as output_file:
                out_csv = csv.writer(output_file)
                out_csv.writerows(in_txt)

for txt_file in glob.glob(txt_files):
    os.remove(txt_file)
    
