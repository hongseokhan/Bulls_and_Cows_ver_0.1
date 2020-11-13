group_list = [['1','2'],['3','4'],['5','6'],['7','8'],['9','0']]
sb_cnt_group_list = [1,1,1,1,0]
test_candidates_list = []
slice_test_candidates_list = []

if len(set(sb_cnt_group_list)) == 2:
    for i in range(len(sb_cnt_group_list)):
        if sb_cnt_group_list[i] == 1:
            test_candidates_list  += str(group_list[i][0])
            print(test_candidates_list)
    for j in range(len(sb_cnt_group_list)):
        slice_test_candidates_list = test_candidates_list[0:2]
        if sb_cnt_group_list[j] == 0:
            test_candidates_list = slice_test_candidates_list + [group_list[j][0],group_list[j][1]]
print(test_candidates_list)
if len(set(sb_cnt_group_list)) == 3:
    for i in range(len(sb_cnt_group_list)):
        if sb_cnt_group_list[i] == 2:
            test_candidates_list += [group_list[i][0],group_list[i][1]]
    for j in range(len(sb_cnt_group_list)):
        if sb_cnt_group_list[j] == 1:
            test_candidates_list += str(group_list[j][0])
print(test_candidates_list)
                            