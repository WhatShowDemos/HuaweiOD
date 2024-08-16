while True:
    try:
        black=list(map(int,input().split()))
        white=list(map(int,input().split()))
        black1=[]
        white1=[]
        for i in range(0,len(black),2):
            co=[black[i],black[i+1]]
            black1.append(co)
        for i in range(0,len(white),2):
            co=[white[i],white[i+1]]
            white1.append(co)
        plate=[[0 for j in range(19)] for i in range(19)]
        for chess in black1:
            plate[chess[0]][chess[1]]=1
        for chess in white1:
            plate[chess[0]][chess[1]]=2
        def qi(x,plate):
            cnt=0
            for i in range(19):
                for j in range(19):
                    if plate[i][j]==0:
                        if i+1<19 and plate[i+1][j]==x:
                            cnt+=1
                        elif i-1>=0 and plate[i-1][j]==x:
                            cnt+=1
                        elif j+1<19 and plate[i][j+1]==x:
                            cnt+=1
                        elif j-1>=0 and plate[i][j-1]==x:
                            cnt+=1
                    else:
                        continue
            return cnt
        black_cnt=qi(1,plate)
        white_cnt=qi(2,plate)
        print('{} {}'.format(black_cnt,white_cnt))
    except:
        break
 
 