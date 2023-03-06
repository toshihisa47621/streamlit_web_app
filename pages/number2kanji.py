import streamlit as st

d1 = {u'1': u'壱', u'2': u'弐', u'3': u'参', u'4': u'四', u'5': u'五', u'6': u'六', u'7': u'七', u'8': u'八', u'9': u'九'}
d3 = {1: u'十', 2: u'百', 3: u'千'}
d4 = {4: u'万', 8: u'億', 12: u'兆'}

def number2kanji(number):
    sio = str(number)
    i = len(sio) - 1
    ret = u""
    for s in sio:
        mod4 = i % 4
        if (mod4 == 0):
            ret += d1.get(s, u"")
            ret += d4.get(i, u"")
        elif (s != u'0'):
            if s != u'1':
                ret += d1.get(s, s)
            else :
                ret += "壱"
            ret += d3.get(mod4, u"")
        i -= 1
    return ret

st.title('数表記変換アプリ')
st.caption('アラビア数字を大字表記の漢数字に変換します')

with st.form(key='enter_form'):
    #変換したい文字を入力する
    before_number = st.text_input('変換したい数を入力し、変換ボタンを押してください')

    #変換ボタン
    exchange_btn = st.form_submit_button('変換')

    after_number = number2kanji(before_number)

    if exchange_btn:
        if after_number=="":
            st.text("0以上9999兆9999億9999万9999以下の整数値を入力してください")
        else:
            st.text(f'変換後：{after_number}')

