def replace_text(lines=None):
    if lines is None:
        lines = ['']
    L = []
    for i in range(len(lines)):
        line = lines[i]
        if 'call char_s' in line:
            content = line[line.index('(') + 1:][:-1].split(',')
            newcontent = line[:line.index('c')] + 'n ' + content[2] + content[3][1:][:-1] + ' ' + content[1]
            lines[i] = newcontent
    return lines


def replace_text_from_file(filename):
    F=open(filename,'r')
    T=F.read().split('\n')
    F.close()
    T=replace_text(T)
    F=open(filename,'w')
    F.write('\n'.join(T))
    F.close()




def main():
    txt='''label check_bus_schedule:
    call char_s(ch_natsuki,"There is a bus line passing near here every half an hour.",4,'c')
    python:'''.split('\n')
    print(replace_text(txt))
    return


if __name__ == "__main__":
    main()
