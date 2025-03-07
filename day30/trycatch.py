try:
    file = open('myfile.txt')
    my_dict = {'key':'value'}
    print(my_dict['key'])

except FileNotFoundError:
    file = open('myfile.txt','w')
    file.write('some text')
    
except KeyError as error_message:
    print(f'the key {error_message} does not exist')

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print('file closed')