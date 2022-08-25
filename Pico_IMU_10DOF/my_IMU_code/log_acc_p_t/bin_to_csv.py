# File : bin_to_csv.py
# to be used with acc_pt_log.py program
# and other similar programs.
#
# Converts acceleration and pressure+temperature binary files
# into csv files
#
# info@pcamus.be
# 22/8/2022

filn_acc_csv="acc.csv"
filn_PT_csv="Press_Temp.csv"

filn_acc="acc.bin"
filn_PT="Press_Temp.bin"

# Reads the first acceleration sample
f_acc_b = open(filn_acc, "rb")
file_buf_acc=f_acc_b.read(6)

f_acc_csv = open(filn_acc_csv, "w")

# While there is something to read
while len(file_buf_acc)==6:
    # Process acceleration samples
    acc_x=file_buf_acc[0]*256+file_buf_acc[1]
    if acc_x>=32767:             
        acc_x=acc_x-65535

    acc_y=file_buf_acc[2]*256+file_buf_acc[3]
    if acc_y>=32767:             
        acc_y=acc_y-65535
        
    acc_z=file_buf_acc[4]*256+file_buf_acc[5]
    if acc_z>=32767:             
        acc_z=acc_z-65535
    
    f_acc_csv.write("%d;%d;%d\n"%(acc_x,acc_y,acc_z))    

    file_buf_acc=f_acc_b.read(6)    

f_acc_b.close()
f_acc_csv.close()

# Reads the first pressure and temperature log
f_PT_b = open(filn_PT, "rb")
file_buf_PT=f_PT_b.read(4)

f_PT_csv = open(filn_PT_csv, "w")

# While there is something to read
while len(file_buf_PT)==4:
    # Process pressure and temperature samples
    pressure = file_buf_PT[0]*256+file_buf_PT[1]
    temperature = (file_buf_PT[2]*256+file_buf_PT[3])/10
    f_PT_csv.write("%d;%4.1f\n"%(pressure, temperature))
    file_buf_PT=f_PT_b.read(4)

f_PT_b.close()
f_PT_csv.close()