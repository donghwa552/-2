import streamlit as st
import random

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(
    page_title="가위바위보 게임",
    page_icon="✌️",
    layout="centered"
)

# -------------------------------
# CSS
# -------------------------------
st.markdown("""
<style>
.stApp{
    background: linear-gradient(180deg,#0B3D91,#1E88E5);
    color:white;
}

h1,h2,h3,p,label,div{
    color:white !important;
}

.stButton>button{
    width:100%;
    background:white;
    color:black !important;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    padding:12px;
    border:none;
}

.stButton>button:hover{
    background:#E3F2FD;
}

.result{
    text-align:center;
    font-size:55px;
    font-weight:bold;
}

.choice{
    text-align:center;
    font-size:80px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 제목
# -------------------------------
st.markdown(
    "<h1 style='text-align:center;'>✌️ 가위바위보 게임</h1>",
    unsafe_allow_html=True
)

st.write("### 무엇을 낼까요?")

# 이모티콘
emoji = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 버튼 3개
col1, col2, col3 = st.columns(3)

user = None

with col1:
    if st.button("✌️ 가위"):
        user = "가위"

with col2:
    if st.button("✊ 바위"):
        user = "바위"

with col3:
    if st.button("✋ 보"):
        user = "보"

# -------------------------------
# 게임 결과
# -------------------------------
if user:

    computer = random.choice(["가위", "바위", "보"])

    if user == computer:
        result = "😐 무승부"

    elif (
        (user == "가위" and computer == "보") or
        (user == "바위" and computer == "가위") or
        (user == "보" and computer == "바위")
    ):
        result = "🎉 승리"
        st.balloons()

    else:
        result = "😢 패배"

    st.markdown("---")

    st.markdown(
        f"<div class='result'>{result}</div>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 😀 나")
        st.markdown(
            f"<div class='choice'>{emoji[user]}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='text-align:center'>{user}</h3>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("### 💻 컴퓨터")
        st.markdown(
            f"<div class='choice'>{emoji[computer]}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='text-align:center'>{computer}</h3>",
            unsafe_allow_html=True
        )

    # 패배 시 비 효과
    if result == "😢 패배":
        st.write("")
        st.markdown(
            "<h1 style='text-align:center;'>🌧️ 🌧️ 🌧️ 🌧️ 🌧️</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<h2 style='text-align:center;'>다음엔 이길 수 있어요!</h2>",
            unsafe_allow_html=True
        )
