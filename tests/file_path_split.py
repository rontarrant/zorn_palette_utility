
# Python program to explain os.path.split() method  
    
# importing os module  
import os 
  
# path 
path = '/home/User/Desktop/file.txt'
  
# Split the path in  
# head and tail pair 
head_tail = os.path.split(path) 
  
# print head and tail 
# of the specified path 
print("Head of '% s:'" % path, head_tail[0]) 
print("Tail of '% s:'" % path, head_tail[1], "\n") 
  
  
# path 
path = '/home/User/Desktop/'
  
# Split the path in  
# head and tail pair 
head_tail = os.path.split(path) 
  
# print head and tail 
# of the specified path 
print("Head of '% s:'" % path, head_tail[0]) 
print("Tail of '% s:'" % path, head_tail[1], "\n") 
  
# path 
path = 'file.txt'
  
# Split the path in  
# head and tail pair 
head_tail = os.path.split(path) 
  
# print head and tail 
# of the specified path 
print("Head of '% s:'" % path, head_tail[0]) 
print("Tail of '% s:'" % path, head_tail[1]) 
