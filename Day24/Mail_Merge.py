names = []
with open('input/names/names.txt') as f:
    names= f.readlines()


with open('input/letters/starting_letter.txt') as f:
    data = f.read()
    for name in names:
        name = name.strip('\n')
        data2 = data.replace('[name]',name)
        with open(f'output/ready_to_send/letter_for_{name}.txt','w') as fd:
            fd.write(data2)
            
