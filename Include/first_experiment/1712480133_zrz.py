from string import ascii_lowercase as lowercase
 
#加密
def VigenereEncrypto (p , key) : 
     p = get_trim_text(p)
     ptLen = len(p)
     keyLen =  len(key)
 
     quotient = ptLen // keyLen    #商
     remainder = ptLen % keyLen    #余
 
     out = ""
 
     for i in range (0 , quotient) :
         for j in range (0 , keyLen) :
             c = int((ord(p[i*keyLen+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
             #global output
             out += chr (c)
 
     for i in range (0 , remainder) :
         c =  int((ord(p[quotient*keyLen+i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
         #global output
         out += chr (c)
 
     return out
     
 #解密
def VigenereDecrypto (output , key) :
     ptLen = len (output)
     keyLen = len (key)
 
     quotient = ptLen // keyLen
     remainder = ptLen % keyLen
 
     inp = ""
 
     for i in range (0 , quotient) :
         for j in range (0 , keyLen) :
             c = int((ord(output[i*keyLen+j]) - ord('a') - (ord(key[j]) - ord('a'))) % 26 + ord('a'))
             #global input
             inp += chr (c)
 
     for i in range (0 , remainder) :
         c = int((ord(output[quotient*keyLen + i]) - ord('a') - (ord(key[i]) - ord('a'))) % 26 + ord('a'))
         #global input
         inp += chr (c)
 
     return inp
     
def get_trim_text(text):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += l
    return trim_text
     
#计算重合指数
def get_coincidence_index(text):
    text = get_trim_text(text)
    length = len(text)
    letter_stats = []
    for l in lowercase:
        lt = {}
        count = text.count(l)
        lt[l] = count
        letter_stats.append(lt)
 
    index = 0
    for d in letter_stats:
        v = list(d.values())[0]
#        index += (float(v)/length) ** 2
        index += (float(v)/length) * (float(v-1)/length-1)
    return index
    
#计算和0.065的差距大小   
def get_var(data, mean=0.065):
    if not data:
        return 0
    var_sum = 0
    for d in data:
        var_sum += (d - mean) ** 2
 
    return float(var_sum) / len(data)
 
#求秘钥长度
def get_key_length(text):
    # assume text length less than 26
    text = get_trim_text(text)
    group = []
    for n in range(1, len(text)+1):
        group_str = ['' for i in range(n)]
        for i in range(len(text)):
            l = text[i]
            for j in range(n):
                if i % n == j:
                    group_str[j] += l
        group.append(group_str)
 
    var_list = []
    length = 1
    for tex in group:
        data = []
        for t in tex:
            index = get_coincidence_index(t)
            data.append(index)
        var_list.append([length, get_var(data)])
        length += 1
    var_list = sorted(var_list, key=lambda x: x[1])
    print(var_list)
    return [v[0] for v in var_list[:int(n/2)+1]]  #var_list[0][0] 
 
 
 
# 统计字母频度
def countList(lis): 
    li = []
    alphabet = [chr(i) for i in range(97,123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count+=1
        li.append(float(count)/len(lis))
    return li
 
# 根据密钥长度将密文分组
def textToList(text,length): 
    text = get_trim_text(text)
    textMatrix = []
    row = []
    index = 0
    for ch in text:
        row.append(ch)
        index += 1
        if index % length ==0:
            textMatrix.append(row)
            row = []
    textMatrix.append(row)
    return textMatrix
    
# 获取密钥
def getKey(text,length): 
    text = get_trim_text(text)
    key = [] # 定义空白列表用来存密钥
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,\
                0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,\
                0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    matrix = textToList(text,length)
    for i in range(length):
        w = [row[i] for row in matrix if len(row) > i] #获取每组密文
        li = countList(w) 
        powLi = [] #算乘积
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k]*li[k]
            powLi.append(Sum)
            li = li[1:]+li[:1]#循环移位
        Abs = 100
        ch = ''
        for j in range(len(powLi)):
             if abs(powLi[j] -0.065546)<Abs: # 找出最接近英文字母重合指数的项
                 Abs = abs(powLi[j] -0.065546) # 保存最接近的距离，作为下次比较的基准
                 ch = chr(j+97)
        key.append(ch)
    return key    
 

def encrypt (message,key):
    key = key.lower()
    non_alpha_count = 0
    cipher = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                offset = ord(key[(i-non_alpha_count)%len(key)]) - ord('a')
                cipher +=chr(((ord(message[i])-ord('A')+offset) % 26) + ord('A'))
            if message[i].islower():
                offset = ord(key[(i-non_alpha_count)%len(key)]) - ord('a')
                cipher +=chr((ord(message[i])-ord('a')+offset) % 26 + ord('a'))
        else:
            cipher +=message[i]
            non_alpha_count +=1
    return cipher



     



def decrypt (message,key):
#    key = key.lower()
    non_alpha_count = 0
    cipher = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                offset = ord(key[(i-non_alpha_count)%len(key)]) - ord('a')
                cipher +=chr(((ord(message[i])-ord('A')-offset) % 26) + ord('A'))
            if message[i].islower():
                offset = ord(key[(i-non_alpha_count)%len(key)]) - ord('a')
                cipher +=chr((ord(message[i])-ord('a')-offset) % 26 + ord('a'))
        else:
            cipher +=message[i]
            non_alpha_count +=1
    return cipher    


if __name__ == '__main__':
    message = input("please enter text: ")
    key = input("please enter key: ")
    words=encrypt(message,key)
    print(words)
    
    key_lengths = []
#    c = input("please enter ciphertext: ")
    key_lengths = get_key_length(words)
    print(key_lengths)
   
    key_len= len(key)
    keys = getKey(words, key_len)
    print(keys)
    print("the plaintext is %s, the length of key is %d, key is %s" \
          % (decrypt(words , keys), key_len, keys))
