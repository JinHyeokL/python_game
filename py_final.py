import tkinter
import random
import time

ITEM = [            #떨어질 단어
    "미래", "가을", "여름", "가치",
    "개척", "가든", "겨울", "고랑",
    "거울", "노을", "누리", "늘찬",
    "단비", "도란", "도움", "두렁",
    "라미", "루비", "리본", "마루",
    "말씨", "마음", "무마", "미라",
    "불꽃", "별빛", "배려", "새녁",
    "샛별", "세찬", "수련", "은하",
    "은빛", "여명", "잎새", "잔별",
    "진로", "친구", "채색", "채움",
    "차원", "기류", "기단", "형태",
    "구원", "생성", "설정", "객체",
    "가람", "가론", "가온", "꽃담",
    "노량", "노을", "느루", "늘봄",
    "다림", "다솜", "다슬", "단미",
    "단춤", "닻별", "라온", "루리",
    "마루", "모아", "믈게", "물꽃",
    "미르", "바림", "별찌", "별하",
    "사품", "샛별", "손갓", "손탁",
    "아라", "아란", "알땀", "초롱",
    "골프", "곱셈", "공익", "광고"
]

ITEM2 = [
    "갈무리", "감또개", "나들목", "내미손",
    "넉걷이", "넘나물", "늦김치", "다님길",
    "도둑눈", "도르리", "도사리", "돋을볕",
    "든해솔", "들때밑", "땅보탬", "마중물",
    "데이트", "비행기", "골짜기", "자스민",
    "합집합", "피크닉", "크로키", "수채화",
    "가그린", "제주도", "클리너", "원주율",
    "맞춤법", "가래떡", "거짓말", "골목길",
    "비주얼", "경복궁", "까마귀", "휴대폰",
    "오작교", "금메달", "은메달", "깍두기",
    "나침반", "낚시꾼", "삼각형", "대장군",
    "루돌프", "마닐라", "줄리엣", "로미오",
    "백화점", "복학생", "전학생", "백록담",
    "보조개", "불문율", "풍선껌", "분홍색",
    "비너스", "블랙홀", "빗방울", "초록색",
    "반려견", "반려자", "소송권", "용의자",
    "블루칩", "설레임", "수영장", "스크린",
    "공수레", "숟가락", "젓가락", "공수거",
    "말리부", "몰디브", "모히또", "치토스",
    "금반지", "은반지", "인물화", "주근깨",
    "장난감", "전투력", "졸업생", "천일염"          #4~6어려운단어
]

ITEM3 = [
    "견인지역", "게르마늄", "공기놀이", "제기차기",
    "강강술래", "술래잡기", "어린이집", "차량운행",
    "안전운전", "안전제일", "퀵서비스", "바른생활",
    "게슴츠레", "고슴도치", "헬리콥터", "오토바이",
    "바이올린", "카멜레온", "오토바이", "파인애플",
    "프로그램", "바로가기", "탱크로리", "사자성어",
    "비밀번호", "가상계좌", "계좌번호", "홈페이지",
    "만사형통", "레이아웃", "신문사설", "영재교육",
    "우리은행", "국민은행", "기업은행", "일본뇌염",
    "폐렴구균", "예방주사", "생년월일", "특별활동",
    "고객센터", "샌드위치", "유통기한", "알레르기",
    "담임교사", "현장학습", "뭉게구름", "호랑나비",
    "종이접기", "휴대전화", "프리미엄", "협동조합",
    "주의사항", "사용방법", "제품설명", "직사광선",
    "분리수거", "폼클렌징", "세숫비누", "빨랫비누",
    "총각김치", "배추김치", "두루치기", "벼룩시장",
    "해바라기", "코스모스", "수면장애", "고지혈증",
    "학습효과", "비선실세", "초등학생", "고등학생",
    "밀폐용기", "후라이팬", "카놀라유", "톱니바퀴",
    "어린이날", "생활용품", "즐겨찾기", "일기예보",
    "무념무상", "공지사항", "헤드라인", "이용약관"        #7~9
]

mouse_x = 0
mouse_y = 0
mouse_c = 0
wf = "Neo둥근모 Pro"
DROP= []        #떨어지는단어
score = 0
yword = ""
index = 0
difficulty = 8
word_number=0
phase=1
start_time=time.monotonic()
make_time=time.monotonic()
Janki = 5
difc = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def make_word(difc):                            #단어 랜덤 생성
    global ITEM, ITEM2, ITEM3
    event_number = random.randint(0,100)
    mk_word = tkinter.Label(root,font=(wf, 15), fg="black", bg="#C2E9F2")
    if difc == 0:
        a=random.randint(0,len(ITEM)-1)
        mk_word["text"]= ITEM[a]
    elif difc == 1:
        a=random.randint(0,len(ITEM2)-1)
        mk_word["text"]= ITEM2[a]
    else:
        a=random.randint(0,len(ITEM3)-1)
        mk_word["text"]= ITEM3[a]
    wx=random.randint(1,750)
    if event_number >= 1 and event_number <4:
        mk_word.config(fg="blue")       #이벤트 단어는 단어색이 파란색
    elif event_number == 4:
        mk_word.config(fg="red")
    elif event_number  >4 and event_number < 7:
        mk_word.config(fg="green")
    mk_word.place(x= wx, y = 20)
    DROP.append(mk_word)                #떨어지는 단어에 추가


def delete_word(lab):
    DROP.remove(lab)
    lab.destroy()
    
def draw_txt(txt, x, y, siz, col, tg):      #텍스트 생성
    fnt = (wf, siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, score, mouse_c, start_time
    global make_time, difficulty
    global phase, Janki, v, a, b, c, difc
    global entry_label, cursor
    if index == 0:
        cvs.delete("gameover")
        a = tkinter.PhotoImage(file="acid.png")
        cvs.create_image(460, 390, image= a, tag="START")
        mouse_c = 0
        index = 1
    elif index == 1:
        if mouse_c == 1:
            b= tkinter.PhotoImage(file="ingame.png")
            cvs.create_image(460, 390, image= b, tag="ingame")
            cvs.delete("START")
            index = 2
            mouse_c = 0
    elif index == 2:   
        game_set()                  #게임화면 세팅
        score_label["text"]= "0점"
        start_time=time.monotonic()     #시작시간 체크
        index = 3
    elif index == 3:
        make_word(difc)
        make_time=time.monotonic()      #단어 생성 주기 체크
        v= random.randint(1,4)
        index = 4
    elif index == 4:
        now = time.monotonic()
        if now-start_time>float(30*phase):          #30초마다 빨라짐
            phase_label["text"]="PHASE"+str(phase+1)
            difficulty=difficulty+2
            phase=phase+1
            if phase == 4 or phase == 7:
                difc = difc+1
        if now-make_time>v:                     #1~4초 랜덤 단어생성
            index=3
        for lab in DROP:                           #단어드랍
            wx=int(lab.winfo_x())
            wy=int(lab.winfo_y())
            wy=wy+difficulty
            lab.place(x=wx,y=wy)
            if wy > 560:                            #선에닿으면 사라짐
                if lab.cget("fg")== "red":
                    Janki = Janki - 2
                score = score - 5
                Janki = Janki - 1
                delete_word(lab)
        score_label["text"]= str(score)+"점"
        Janki_label["text"]= "남은목숨 : "+str(Janki)
        if Janki <= 0:
            index = 5
    elif index == 5:
       game_end()     #게임 종료 화면 정의
       index= 6
    elif index == 6:
        if 350 <= mouse_x and mouse_x < 450 and mouse_y >=500 and mouse_y < 612:
            cvs.delete("CURSOR")
            if mouse_c == 1:
                score_label.destroy()
                index = 0
                mouse_c = 0
            cvs.create_image(405, 590, image=cursor, tag="CURSOR")
        elif 470 <= mouse_x and mouse_x < 570 and mouse_y >=500 and mouse_y < 612:
            cvs.delete("CURSOR")
            cvs.create_image(520, 590, image=cursor, tag="CURSOR")
            if mouse_c == 1:
                root.quit()
        else:
            cvs.delete("CURSOR")
            mouse_c = 0
    entry_word.bind("<KeyPress>", key_down)
    root.after(100,game_main)

def game_set():
    global score_label, entry_word, phase_label, Janki_label, entry_label
    global Janki, score, start_time, difc, make_time, difficulty, now, phase
    score_label = tkinter.Label(root, font=(wf, 32), bg="#f9f9ee")
    score_label.place(x=750, y=80)
    entry_label = tkinter.Label(root,text="입력 : ", font=(wf, 14),bg="#ddffe5")
    entry_label.place(x=305,y=620)
    entry_word.place(x=370,y=620)
    entry_word.focus()                  #시작하자마자 입력창에 커서
    phase_label = tkinter.Label(text="PHASE"+str(phase),font=(wf, 14), bg="#e6e6db")
    phase_label.place(x=60,y=35)
    cvs.create_line(0,590,912,590, fill="")
    Janki_label = tkinter.Label(root, font=(wf, 12), bg="#c7c7ae")
    Janki_label.place(x= 770, y=35)
    Janki = 5
    score = 0
    phase = 0
    start_time = 0
    difc = 0
    make_time = 0
    difficulty = 8
    now = 0

def game_end():   #게임 종료 화면
    global entry_word, entry_label, phase_label, Janki_label, score_label
    global c, index, mouse_c, mouse_x, mouse_y
    cvs.delete("ingame")
    for lab in DROP:
        lab.destroy()
    entry_word.place(x=-100,y=-100)
    entry_label.destroy()
    phase_label.destroy()
    Janki_label.destroy()
    score_label.place(x=400, y=380)
    score_label.config(bg="black", fg="#42c75d")
    DROP.clear()
    c= tkinter.PhotoImage(file="gameover.png")
    cvs.create_image(460, 390, image= c, tag="gameover")

def key_down(e):
    global score, yword, entry_word, Janki, difficulty
    key = e.keysym
    if key == "Return":     #엔터판별
        k=0
        yword= entry_word.get()
        for lab in DROP:          #입력값 판별
            w = lab.cget("text")
            if yword == w:
                if lab.cget("fg")=="blue":      #이벤트 단어 판별
                    Janki = Janki + 1
                elif lab.cget("fg")=="green":
                    score = score + difficulty
                score = score + difficulty
                k=k+1
                delete_word(lab)
        if k == 0: score = score -5
        entry_word.delete(0, tkinter.END)

root = tkinter.Tk()
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
root.title("산성비 게임")
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.resizable(False, False)
entry_word = tkinter.Entry(root, width=20, font=(wf, 15))
cursor = tkinter.PhotoImage(file="kitty_cursor.png")
game_main()
root.mainloop()
