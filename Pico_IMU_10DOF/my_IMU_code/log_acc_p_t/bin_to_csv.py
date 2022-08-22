# File : bin_to_csv.py
# to be used with icm20948_lps22hb_speed_test.py program
# and other similar programs.
#
# Converts acceleration and pressure+temperature binary files
# into csv files
#
# Only for one 10 s sample. To be extended to full file
#
# info@pcamus.be
# 22/8/2022

filn_acc_csv="acc.csv"
filn_PT_csv="Press_Temp.csv"

filn_acc="acc.bin"
filn_PT="Press_Temp.bin"

# Reads the first 10 sec acceleration log
f = open(filn_acc, "rb")
file_buf_acc=f.read(600)
f.close()

# Reads the first pressure and temperature log
f = open(filn_PT, "rb")
file_buf_PT=f.read(4)
f.close()

f = open(filn_acc_csv, "w")

# Process acceleration samples
for i in range(100):
    buf_index=i*6
    acc_x=file_buf_acc[buf_index]*256+file_buf_acc[buf_index+1]
    if acc_x>=32767:             
        acc_x=acc_x-65535

    acc_y=file_buf_acc[buf_index+2]*256+file_buf_acc[buf_index+3]
    if acc_y>=32767:             
        acc_y=acc_y-65535
        
    acc_z=file_buf_acc[buf_index+4]*256+file_buf_acc[buf_index+5]
    if acc_z>=32767:             
        acc_z=acc_z-65535
    
    f.write("%d;%d;%d\n"%(acc_x,acc_y,acc_z))
    
f.close();

# Process pressure and temperature samples
pressure = file_buf_PT[0]*256+file_buf_PT[1]
temperature = (file_buf_PT[2]*256+file_buf_PT[3])/10

f = open(filn_PT_csv, "w")
f.write("%d;%4.1f\n"%(pressure, temperature))
f.close()