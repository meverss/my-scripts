def find_common_characters(msg1,msg2):
    l=[]
    msg11=msg1.replace(" ", "")
    msg22=msg2.replace(" ", "")
    for letter in msg11:
        if letter in msg22:
            l.append(letter)
            if len(l)!=0:
                return "".join(l)
            else:
                return -1

msg1="SoloLearn"# Learning LearningIsFun Learnable"
msg2="Learning"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)