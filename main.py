import os




def read_file(file_name, start=None, end=None):
    
    file = open(file_name,'rb')
    if start != None and end != None:

    	return [str(i) for i in file.readlines()[int(start):int(end)]]
    else:
        return [str(i) for i in file.readlines()]
    
    
    