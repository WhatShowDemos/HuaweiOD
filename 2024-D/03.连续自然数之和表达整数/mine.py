import sys
from collections import namedtuple
 
def writeeq(num):
    eq_num = 0;
    
    for last in range(num, 0, -1):
        if last == num:
            eq_num = eq_num + 1;
            print(str(num) + "=" + str(num));
        elif last > 1:
            nums = [str(last)];
            last_sum = last;
            for last2 in range(last-1, 0, -1):
                last_sum = last_sum + last2;
                nums.insert(0, str(last2));
                if last_sum == num:
                    eq_num = eq_num + 1;
                    eles = "+".join(nums);
                    print(str(num) + "=" + eles);
                    break;
                if last_sum > num:
                    break;
    print("Results:" + str(eq_num));
    
    
if __name__ == "__main__":
    writeeq(9);
    print();
    writeeq(10);
    print();
    writeeq(1);
    print();