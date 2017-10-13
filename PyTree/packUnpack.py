def packer(**kwargs): #key word args, double asterix tells it to pack all the values
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}".format(first_name, last_name))

    else:
        print("Who are you? Koi bhi nahi")


packer(name='Kenneth', num=42 , spanish_aquisition=None)

unpacker(**{'last_name':'Jha', 'first_name':'Vik'})#the ** sent the dictionary to the function as an argument
