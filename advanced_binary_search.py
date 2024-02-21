# original query
s1 = '0010110'

def find_compliment(inp_string):
    new_string = ''
    for i in inp_string:
        if i == '0':
            new_string += '1'
        else:
            new_string += '0'
            
    return new_string
            
print(f"Original String: {s1}")
print(f"Complement: {find_compliment(s1)}\n\n")


def build_nth_string(s0, n):
    mod_string = s0
    for i in range(n):
        mod_string = mod_string + '0' + find_compliment(mod_string)
        
    return mod_string
    

def search_kth_index(mod_string, k):
    return mod_string[k]

n = 2000
k = 4
s0 = '0'

mod_string = build_nth_string(s0, n)
print(mod_string)

print(search_kth_index(mod_string, k))

    
    
