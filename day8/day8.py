def map_first(input_digs, char_mapping):
    for num in input_digs:
        if len(num) == 2:
            char_mapping[1] = [c for c in num]
        if len(num) ==3:
            char_mapping[7] = [c for c in num]
        if len(num)==4:
            char_mapping[4] = [c for c in num]
        if len(num) == 7:
            char_mapping[8] = [c for c in num]

def map_second(input_digs,char_mapping):
    for num in input_digs:
        if len(num) == 5 and chars_in_list(char_mapping[1],num):
            char_mapping[3] = [c for c in num]
    for num in input_digs:
        if len(num) == 6 and chars_in_list(char_mapping[3],num):
            char_mapping[9] = [c for c in num]
        elif len(num)==6 and not chars_in_list(char_mapping[7],num):
            char_mapping[6] = [c for c in num]
    for num in input_digs:
        if len(num) == 5:
            if chars_in_list(char_mapping[1],num):
                continue
            if chars_in_list(num,char_mapping[6]):
                char_mapping[5] = [c for c in num]
            else:
                char_mapping[2] = [c for c in num]
        if len(num)==6 and chars_in_list(char_mapping[7],num) and not chars_in_list(char_mapping[9], num):
            char_mapping[0] = [c for c in num]

def calc_output(output_digs, char_mapping):
    out = ""
    for num in output_digs:
        for char,mapp in char_mapping.items():
            if len(num) == len(mapp) and chars_in_list(num,mapp):
                out += str(char)
    return out
def chars_in_list(chars, mapp):
    for c in chars:
        if c not in mapp:
            return False
    return True

with open("input.txt") as f:
    lines = f.readlines()
    total=0
    for line in lines:
        data = line.strip().split('|')
        input_digs = data[0].split() + data[1].split()
        output_digs = data[1].split()
        char_mapping={}
        map_first(input_digs,char_mapping);
        map_second(input_digs,char_mapping);
        output = calc_output(output_digs, char_mapping);
        total += int(output)
    print(total)
