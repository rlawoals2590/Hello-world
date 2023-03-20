import random
import time

en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
text = 'hello world'

for i in en:
    time.sleep(0.02)
    print(i)
    if i == text[0]:
        a = i
        for i in en:
            time.sleep(0.02)
            print(a + i)
            if i == text[1]:
                b = i
                for i in en:
                    time.sleep(0.02)
                    print(a + b + i)
                    if i == text[2]:
                        c = i
                        for i in en:
                            time.sleep(0.02)
                            print(a + b  + c + i)
                            if i == text[3]:
                                d = i
                                for i in en:
                                    time.sleep(0.02)
                                    print(a + b + c + d + i)
                                    if i == text[4]:
                                        e = i
                                        for i in en:
                                            time.sleep(0.02)
                                            print(a + b + c + d + e +' '+ i)
                                            if i == text[6]:
                                                f = i
                                                for i in en:
                                                    time.sleep(0.02)
                                                    print(a + b + c + d + e +' '+ f + i)
                                                    if i == text[7]:
                                                        g = i
                                                        for i in en:
                                                            time.sleep(0.02)
                                                            print(a + b + c + d + e +' '+ f + g + i)
                                                            if i == text[8]:
                                                                h = i
                                                                for i in en:
                                                                    time.sleep(0.02)
                                                                    print(a + b + c + d + e +' '+ f + g + h + i)
                                                                    if i == text[9]:
                                                                        q = i
                                                                        for i in en:
                                                                            time.sleep(0.02)
                                                                            print(a + b + c + d + e +' '+ f + g + h + q + i)
                                                                            if i == text[10]:
                                                                                j = i
                                                                                print(a + b + c + d + e +' '+ f + g + h + q + j)
                                                                                break
                                                                            
                                                                        
            