files = ["in1", "in2", "in3"]
out_accs = ["3", "2", "2"]

for file in files:
    f = open(file)
    
    N = int(f.readline());
    
    words = [];
    for i in range(N):
        words.append(f.readline().strip())
    chars = f.readline().strip();
    chars_norm = chars.replace('?', '');
    chars_q_num = chars.count('?')
    
    word_num = 0;
    for word in words:
        tmp_char = chars_norm;
        mis_num = 0;
        for i in range(len(word)):
            if word[i] in tmp_char:
                char_i = tmp_char.index(word[i])
                tmp_char = tmp_char[:char_i] + tmp_char[char_i+1:]
            else:
                mis_num +=1;
        if mis_num <= chars_q_num:
            word_num+=1;
    print(word_num);
    
    f.close();
    
print("Accurate: ")
for out_acc in out_accs:
    print(out_acc)