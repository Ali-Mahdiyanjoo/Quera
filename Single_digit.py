single_digit = int(input())
single_digit_list = list(str(single_digit))

if single_digit > 9:
    single_sum = sum(map(int, single_digit_list))
    if single_sum > 9:
        single_sum_2 = sum(map(int, list(str(single_sum))))
        if single_sum_2 > 9:
            single_sum_3 = sum(map(int, list(str(single_sum_2))))
            print(single_sum_3)
        else:
            print(single_sum_2)
    else:
        print(single_sum)
else:
    print(single_digit)