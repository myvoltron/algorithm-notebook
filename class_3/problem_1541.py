str = input()

result = 0
index = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        currnet_number = str[index]
        index += 1
        while index < len(str):
            if str[index] == "+" or str[index] == "-":
                break
            currnet_number += str[index]
            index += 1
        result += int(currnet_number)
    elif str[index] == "+":
        index += 1
        continue
    else:
        current_sum = 0
        index += 1
        while index < len(str) and str[index] != "-":
            if str[index] >= "0" and str[index] <= "9":
                currnet_number = str[index]
                index += 1
                while index < len(str):
                    if str[index] == "+" or str[index] == "-":
                        break
                    currnet_number += str[index]
                    index += 1
                current_sum += int(currnet_number)
            elif str[index] == "+":
                index += 1
                continue
        result -= current_sum

print(result)
