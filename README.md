# 📝 DokiDoki Diary  
あなたの毎日を “声” と AI で彩る、**Streamlit 製パーソナル日記アプリ**

---

## 📷 概要
**DokiDoki Diary** は “話す → 書く → 振り返る” までをワンストップで支援する  
パーソナル日記 Web アプリです。  
音声入力を Whisper で文字起こしし、GPT‑4o mini がチュートリアル徳井義実
（関西弁）になりきってフィードバック。  
さらに DALL·E 3 がその日の思い出をイラスト化し、SQLite に保存された
日記を 1 ヶ月前・1 年前と並べて振り返れます。  
Tech0 9 期 Step 2‑2「Streamlit アプリ開発」課題作品として作成しました。

---

## ✨ 主な機能
| 機能 | 説明 |
|------|------|
| 音声入力 | `audio_recorder_streamlit` で録音し、OpenAI Whisper API で文字起こし :contentReference[oaicite:0]{index=0} |
| AI フィードバック | GPT‑4o mini が<br>選択した「癒し / 励まし / 喝」モード & 徳井義実キャラでコメント生成 :contentReference[oaicite:1]{index=1} |
| 天気連動アドバイス | つくみじま天気 API から埼玉県さいたま市の予報を取得し、必要に応じてコメントへ反映 :contentReference[oaicite:2]{index=2} |
| 思い出イラスト | DALL·E 3 で Toy Story 風のイラストを自動生成 :contentReference[oaicite:3]{index=3} |
| データ保存 & リフレクション | SQLite に `Diary_table` を作成し、当日 / 1 ヶ月前 / 1 年前の日記＋FB を比較表示 :contentReference[oaicite:4]{index=4} |

---

## 🚀 クイックスタート

```bash
# 1. リポジトリを取得
git clone https://github.com/aripoyo14/dokidoki_diary.git
cd dokidoki_diary

# 2. 依存パッケージをインストール
pip install -r requirements.txt        # streamlit, openai, etc. :contentReference[oaicite:5]{index=5}

# 3. OpenAI API キーを渡す
#   いずれか好きな方法で設定してください
echo -e "[openai]\napi_key = \"sk-...\"" > .streamlit/secrets.toml
#   もしくは環境変数 OPENAI_API_KEY に設定

# 4. アプリを起動
streamlit run dokidoki_diary.py
