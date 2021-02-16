testfile2 = 'Week2files/writetome.csv'
touples = {('write this at line 1'), ('i am the second line'), ('i dont care')}

def write_list_to_file(output_file, touples):
    with open(output_file) as file_object:
        for x in touples:
            file_object.write(x + '\n')
            
write_list_to_file(testfile2, touples)
