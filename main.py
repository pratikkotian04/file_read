import os




def read_file(file_name, start=None, end=None):
    try:
        file = open(file_name,'rb')
        if start != None and end != None:

            return [str(i) for i in file.readlines()[int(start):int(end)]]
        else:
            return [str(i) for i in file.readlines()]
        
    except:
        return ["<b>Error is file reading.Please sepcify another file</b>"]
    
    
    