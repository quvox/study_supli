# from grade6_lv2 import chapters_japanese as chapters
# from grade6_lv2 import chapters_science as chapters
from grade6_lv2 import chapters_social as chapters

#from grade6_basic import chapters_math as chapters
#from grade6_basic import chapters_japanese as chapters
#from grade6_basic import chapters_science as chapters
#from grade6_basic import chapters_math as chapters
#from grade6_basic import chapters_social as chapters

#from grade5_lv0 import chapters_math as chapters
#from grade5_lv2 import chapters_math as chapters
#from grade5_lv2 import chapters_japanese as chapters
#from grade5_lv2 import chapters_science as chapters
#from grade5_lv2 import chapters_social as chapters
#from grade5_basic import chapters_math as chapters

exam_included = True   # 各講座に確認テストがあるかどうか

chapter_num_per_day = 4
chapter_num_per_day = 3
chapter_num_per_day = 2
only_same_class_in_day = False  # 1日に複数の講座をまたがないようにしたい場合はTrueにする(理社の場合を想定)


outputs = list()  # 出力文字列
for sec, c_num in enumerate(chapters):
    for x in range(c_num):
        outputs.append(f"{sec+1}-{x+1}")
    if chapter_num_per_day:
        outputs.append(f"{sec+1}-確")

while len(outputs) > 0:
    line = list()
    for i in range(chapter_num_per_day):
        if len(outputs) == 0:
            break
        txt = outputs.pop(0)
        line.append(txt)
        if only_same_class_in_day and len(outputs) > 0:
            txt2 = outputs[0].split("-")[0]  # 次のチャプターの講座番号を取得して、比較する
            if txt[:len(txt2)] != txt2:
                break   # 別の講座になるようならその日には入れない


    print("、".join(line))
