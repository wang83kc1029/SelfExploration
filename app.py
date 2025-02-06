import streamlit as st
from openai import OpenAI

# 設定 OpenAI API
client = OpenAI(api_key=st.secrets["openai"]["api_key"])
model = "gpt-4o-mini"
with open("system_content.txt", "r", encoding="utf-8") as file:
    system_content = file.read()

# UI
st.title("自我探索 / Self Exploration")
user_story = st.text_area("請輸入你的故事 / Enter your story：", height=400)

# 範例故事
with st.expander("範例故事"):
    with open("example_story.txt", "r", encoding="utf-8") as file:
        st.text(file.read())

with st.expander("Example Story"):
    with open("example_story_en.txt", "r", encoding="utf-8") as file:
        st.text(file.read())

if st.button("分析故事 / Analyze story"):
    prompt = f"""我的故事裡面有哪些比較負面的潛在信念呢？

    {user_story}
    
    use English to respond only when the story is in English。
    """

    result = (
        client.chat.completions.create(
            model=model,
            store=True,
            messages=[
                {
                    "role": "system",
                    "content": system_content,
                },
                {"role": "user", "content": prompt},
            ],
        )
        .choices[0]
        .message.content
    )
    st.write(result)
