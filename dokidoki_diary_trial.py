import streamlit as st
import datetime
from openai import OpenAI
# import sqlite3
# from dotenv import load_dotenv
# import os

# .envファイルから環境変数を読み込む
# load_dotenv()

# 左上のロゴ（さやさんデザインを仮で使用）
st.logo(
    "images_master/team_dokidoki_logo.png",
)

# 徳井風のイケメン（DALL-E3作※2回作ったら1日分のトークンが無くなった）
st.image("images_master/tokui_ver1.png") #,caption="Team DokiDoki")

# 小さい列と大きい列を作成
question_col, date_col = st.columns([25, 5])  # [25, 5]は列の比率

# question列に日記記入を促す文を入れる
with question_col:
    st.markdown('<div style="font-size: 24px; text-align: center;">お疲れ様。今日はどんな1日だった？</div>', unsafe_allow_html=True)

# date列に日付入力欄を入れる
with date_col:
    date = st.date_input("")

# 日記を入力する欄を入れる。openaiに渡したり、日記内容を反映した画像と合わせて日記を表示するためにdiary_inputに日記内容を代入する。
diary_input = st.text_area("日記を入力する", height=150 ,label_visibility="hidden", placeholder="マイクに話しかけてね。ちょっと違う部分は手動で編集してね。ごめんね。")
# 送信ボタンを入れる
submit_btn = st.button("今日の日記生成")

#送信ボタンが押されると以下の処理が走る
if submit_btn:
    # 列を2つに分割する
    col1, col2 = st.columns(2)

    # 左の列には絵日記を表示。imageのところにopenaiで生成した画像を渡す。
    with col1:
        # dall-e-3で日記内容を反映したイラストを作成
        #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        api_key = st.secrets["openai"]["api_key"]
        client = OpenAI(api_key=api_key)
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Create a cute illustration based on the following text. \n #text \n {diary_input}",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        image = image_url
        st.image(image, width=300)

    # 右の列には日記とフィードバックを表示
    with col2:
        st.write("Your Diary（日記に入力した内容がそのまま表示される）")
        # 文章を枠で囲う処理を入れています。
        st.markdown("""                    
                    <div style="background-color: #F0F2F6; padding: 15px; border-radius: 5px;">
                        diary_input
                    </div>
                    """, unsafe_allow_html=True)

        st.write("Feedback from Tokui")
        feedback = "フィードバック（Openai APIで生成したフィードバックをここに格納する）"
        st.markdown("""                    
                    <div style="background-color: #F0F2F6; padding: 15px; border-radius: 5px;">
                        フィードバックが表示される
                    </div>
                    """, unsafe_allow_html=True)
    '''    
    conn = sqlite3.connect('dokidoki_diary.db')
    cur = conn.cursor()

    data = (1, date, diary_input, feedback, image)
        

    cur.execute(
        "INSERT INTO Diary_table (user_id, date, diary, feedback, illustration) VALUES (?,?,?,?,?)",
        data
    )

    conn.commit()
    conn.close()
    '''
    