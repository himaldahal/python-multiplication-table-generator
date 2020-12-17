# Table Generator Python
# Made By Himal Dahal
startTable = int(input('Start Table from : '))
endTable = int(input('End Table at : '))
fileName = str(input('Enter File Name to save as > '))
    
print('Table Generation Started.')    
for i in range(startTable,(int(endTable) + int(1))):    
              
    for tnum in range(1,11):
      with open(fileName  + str('.txt') ,'a') as f:
          f.write(f'{i} X {tnum} = ' + str(i * tnum) + '\n')
    
    with open(fileName  + str('.txt') ,'a') as f:
          f.write('\n\n')         
          
    
    
print('Table generated Successfuly')    
    
