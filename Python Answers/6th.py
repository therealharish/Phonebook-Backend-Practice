import sys
import string

def reverse_fizz_buzz(input) :

    values = {}
    factors = []
    highest_factor = {}
    #Setup a complete List of factors
    for line in input :
        temp_factors = {}
        for char in line :
            highest_factor[char] = highest_factor.get(char, 0) + 1
            temp_factors[char] = highest_factor[char]
        factors.append(temp_factors)

    i = 0
    highest_val = 0
    #itterate forward as many times as nessessary
    while i < len(factors) :
        if i == 0 :
            for key in factors[i].keys() :
                values[key] = 1
            i += 1
            continue
        # compare previous line to current
        prev_key = list(factors[i - 1])[0]
        cur_key = list(factors[i])[0]
        total_prev = values[prev_key] * factors[i - 1][prev_key]
        total_cur = values.get(cur_key, 0) * factors[i][cur_key]
        highest_val = max(highest_val,total_cur)
        if total_prev >= total_cur :
            # too low, adjust
            values[cur_key] = int(total_prev / factors[i][cur_key] + 1)
            #return to previous instance of key if it exists and retry
            i = 1
            continue

        # check equality on same line
        current_keys = list(factors[i])
        modified = False
        for j,x in enumerate(current_keys[:len(current_keys) - 1]) :
            for y in current_keys[j + 1:len(current_keys)] :
                total_x = values.get(x,0) * factors[i][x]
                total_y = values.get(y,0) * factors[i][y]
                if total_x == total_y :
                    continue
                elif total_x < total_y :
                    values[x] = max(int(total_y / factors[i][x]),values.get(x,0) + 1)
                    highest_val = max(highest_val,values[x] * factors[i][x])
                    modified = True
                else :
                    values[y] = max(int(total_x / factors[i][y]),values.get(y,0) + 1)
                    highest_val = max(highest_val,values[y] * factors[i][y])
                    modified = True
        if modified :
            i = 1
            continue
        else :
            i += 1
    lower = string.ascii_lowercase
    highest_letter_found = False
    for char in lower[::-1] :
        if values.get(char,0) > 0:
            highest_letter_found = True
        elif highest_letter_found :
            values[char] = highest_val + 1
    # print (list(values.items()).sort(key = lambda x : x[0]))
    temp = (sorted(values.items(), key=lambda kv:
                 kv[0]))
    res = []
    for i in temp:
        res.append(i[1])
    print(res)
reverse_fizz_buzz(['c', 'ce', 'd', 'c', 'ce', 'd', 'c', 'a', 'ce', 'cd', 'b', 'ce', 'c', 'd', 'ce', 'c', 'a', 'd', 'ce', 'c', 'cde', 'c', 'b', 'ce', 'd', 'ac', 'ce', 'd', 'c', 'ce', 'cd', 'ce', 'a', 'bc', 'd', 'ce', 'c', 'd', 'ce', 'c', 'cde', 'a', 'c', 'ce', 'df', 'b', 'c', 'ce', 'd', 'c', 'ace', 'cd', 'ce', 'c', 'd', 'ce', 'b', 'c', 'ad', 'ce', 'c'])  