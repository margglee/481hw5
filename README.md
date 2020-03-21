# 481hw5
download libpng
testall runs files in current dir
python3 ../hw5/delta.py 54 bash ../hw5/is-minimize.sh 


### For a subset of 10 images (0-9)
run-all.sh on entire subset gave 19.73% coverage  
delta.py/is-minimize.sh selected images [0, 4, 6]  
run-all.sh on [0, 4, 6] gave 19.73% coverage  
delta-min.py/dataDict10.txt selected images [0, 1, 2]  
run-all.sh on [0, 1, 2] gave 19.68% coverage  


### For a subset of 20 images (0-19)
run-all.sh on entire subset gave 19.75% coverage  
delta.py/is-minimize.sh selected images [0, 11]  
run-all.sh on [0, 11] gave 15.50% coverage  
delta-min.py/dataDict20.txt selected images [0, 1, 2, 4]  
run-all.sh on [0, 1, 2, 4] gave 19.72% coverage  


### For a subset of 30 images (0-29)
run-all.sh on entire subset gave 19.75% coverage  
delta.py/is-minimize.sh selected images [0, 11]  
run-all.sh on [0, 11] gave 15.50% coverage  
delta-min.py/dataDict20.txt selected images [0, 2, 4]  
run-all.sh on [0, 2, 4] gave 19.72% coverage  


### For a subset of 40 images (0-39)
run-all.sh on entire subset gave 19.75% coverage  
delta.py/is-minimize.sh selected images [0, 11]  
run-all.sh on [0, 11] gave 15.50% coverage  
delta-min.py/dataDict20.txt selected images [0, 1, 2, 4]  
run-all.sh on [0, 1, 2, 4] gave 19.72% coverage  


### For a subset of 50 images (0-49)
run-all.sh on entire subset gave 23.02% coverage  
delta.py/is-minimize.sh selected images [0, 4, 44]  
run-all.sh on [0, 4, 44] gave 23.00% coverage  
23.02% coverage calculated from python dictionary of gcov info for entire subset  
delta-min.py/dataDict50.txt selected images [0, 38]  
run-all.sh on [0, 38] gave 19.68% coverage  


### For a subset of 100 images (0-99)
run-all.sh on entire subset gave 25.18% coverage  
delta.py/is-minimize.sh selected images [0, 11, 70, 84, 85, 86, 89, 95, 96, 98]  
run-all.sh on [0, 11, 70, 84, 85, 86, 89, 95, 96, 98] gave 23.79% coverage  


### For all 1639 images
run-all.sh on entire subset gave 37.97% coverage  
delta.py/is-interesting forced termination due to excessive run time > 15 hours  
delta-min.py/dataDict1639.txt selected images [11, 55, 249, 289, 295, 313, 373, 446, 508, 509, 515, 516, 517, 569, 572, 587, 682, 729, 739, 899, 941, 942, 952, 963, 964, 990, 1077, 1161, 1191, 1200, 1212, 1221, 1229, 1237, 1247, 1253, 1303, 1307, 1317, 1318, 1321, 1358, 1370, 1443, 1448, 1471]  
run-all.sh on 46 images selected by delta-min.py/dataDict1639.txt gave 34.30% coverage   
378 calls to is-interesting()     
time for delta-min.py/dataDict1639.txt:  
time python3 delta-min.py 1639 dataDict1639.txt > output    
real    84m7.520s     
user    82m50.578s    
sys     0m9.047s 