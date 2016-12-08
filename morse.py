import winsound
import time
Freq = 550
Dur = 60
Array_V = ( [1, 3],             # A Index = 0
            [3, 1, 1, 1],       # B Index = 1
            [3, 1, 3, 1],       # C Index = 2
            [3, 1, 1],          # D Index = 3
            [1],                # E Index = 4
            [1, 1, 3, 1],       # F Index = 5
            [3, 3, 1],          # G Index = 6
            [1, 1, 1, 1],       # H Index = 7
            [1, 1],             # I Index = 8
            [1, 3, 3, 3],       # J Index = 9
            [3, 1, 3],          # K Index = 10
            [1, 3, 1, 1],       # L Index = 11
            [3, 3],             # M Index = 12
            [3, 1],             # N Index = 13
            [3, 3, 3,],         # O Index = 14
            [1, 3, 3, 1],       # P Index = 15
            [3, 3, 1, 3],       # Q Index = 16
            [1, 3, 1],          # R Index = 17
            [1, 1, 1],          # S Index = 18
            [3],                # T Index = 19
            [1, 1, 3],          # U Index = 20
            [1, 1, 1, 3],       # V Index = 21
            [1, 3, 3],          # W Index = 22
            [3, 1, 1, 3],       # X Index = 23
            [3, 1, 3, 3],       # Y Index = 24
            [3, 3, 1, 1]        # Z Index = 25
            )
Array_N = ( [1, 3, 3, 3, 3],    # 0 Index = 0
            [1, 1, 3, 3, 3],    # 1 Index = 1
            [1, 1, 1, 3, 3],    # 2 Index = 2
            [1, 1, 1, 1, 3],    # 3 Index = 3
            [1, 1, 1, 1, 1],    # 4 Index = 4
            [3, 1, 1, 1, 1],    # 5 Index = 5
            [3, 3, 1, 1, 1],    # 6 Index = 6
            [3, 3, 3, 1, 1],    # 7 Index = 7
            [3, 3, 3, 3, 1],    # 8 Index = 8
            [3, 3, 3, 3, 3]     # 9 Index = 9
            )			

InputChar = input("Input what to show: ").upper()   # 全轉大寫
Target = InputChar.split()                          # 分割字串(空格)

def SpeakerBeep(MorseCode):
    Duration = Dur * MorseCode
    print("MorseCode = ", MorseCode, "Duration = ", Duration)
    winsound.Beep(Freq, Duration)
    time.sleep(Dur/1000)
	
def MorseDecode(ArrayContent):
    for i in ArrayContent:              #逐字解 MorseCode
        print(i)
        if 90 >= ord(i) >= 65:          # 判斷是字母還是數字
            Index = ord(i) - 65
            InnerArr = Array_V[Index]   # 根據解出來的ASCII查表
            InnerArrLen = len(InnerArr)
            for j in InnerArr:          # 傳表進 SpeakerBeep
                SpeakerBeep(j)
        elif 48 <= ord(i) <= 57:        # 判斷是字母還是數字
            Index = ord(i) - 48
            InnerArr = Array_N[Index]
            InnerArrLen = len(InnerArr)
            for j in InnerArr:
                SpeakerBeep(j)	
        else:                           # 不是字母也不是數字
            print("input over range")
            winsound.Beep(Freq,Dur)
    time.sleep((Dur/1000)*7)            # 每個 parse 出來的字組都要間隔 7倍 間隔時間

for ArrayContent in Target:             # 傳 parse 過的字組 list 進 MorseCode
    MorseDecode(ArrayContent)