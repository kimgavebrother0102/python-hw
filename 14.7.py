 korean, english, math, science=map(int,input().split())
 x=(korean+english+math+science)/4
 if korean>100 or english>100 or math>100 or science>100 or korean<0 or english<0 or math<0 or science<0
     print('잘못된 점수')
else:
    if x>=80:
        print('합격')
    else x<80:
        print('불합격')
