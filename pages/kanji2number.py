import streamlit as st

KANJI1 = "零壱弐参四五六七八九"
KANJI2 = "拾百千"
KANJI3 = "万億兆"
INT1 = {kanji: i for i, kanji in enumerate(KANJI1)}
INT2 = {kanji: 10**i for i, kanji in enumerate(KANJI2, 1)}
INT3 = {kanji: 10000**i for i, kanji in enumerate(KANJI3, 1)}

def kanji_to_int(kanji):
    i1 = i2 = i3 = 0
    for k in kanji:
        if k in KANJI1:
            i1 = i1 * 10 + INT1[k]
        elif k in KANJI2:
            i2 += (i1 or 1) * INT2[k]
            i1 = 0
        elif k in KANJI3:
            i3 += (i1 + i2 or 1) * INT3[k]
            i1 = i2 = 0
        else:
            i1 = i2 = i3 = 0
            break
    return i1 + i2 + i3


st.title('数表記変換アプリ')
st.caption('大字表記の漢数字をアラビア数字に変換します')

with st.form(key='enter_form'):
    #変換したい文字を入力する
    before_kanji = st.text_input('変換したい漢数字を入力し、変換ボタンを押してください')

    #変換ボタン
    exchange_btn = st.form_submit_button('変換')

    after_kanji = kanji_to_int(before_kanji)
    

    if exchange_btn:
        if after_kanji==0:
            st.text("大字表記の漢数字を入力してください")
        else:
            st.text(f'変換後：{after_kanji}')