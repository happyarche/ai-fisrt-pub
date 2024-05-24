#환경변수 호출
# from dotenv import load_dotenv
# load_dotenv()


# import os
import sys
import streamlit as st
import time

from langchain_openai import OpenAI

# 콘솔 인코딩 설정을 UTF-8로 변경
sys.stdout.reconfigure(encoding='utf-8')

# OpenAI LLM 인스턴스 생성
llm = OpenAI()

st.title('오늘 뭐 먹지?')

content = st.text_input("언제 먹을 메뉴를 고르고 있나요?", "오늘 저녁")
st.write(content,"에 먹을 메뉴를 추천해 드리겠습니다. 추천 버튼을 클릭하세요" )


if st.button("추천하기"):
    with st.spinner('Wait for it...'):
     result = llm.invoke(content+" 뭐먹지? 메뉴 하나 추천해주고, 레시피도 알려줘")
     st.write(result)


# result = llm.invoke(content+" 뭐먹지? 추천해주고, 레시피도 알려줘")
# print(result)






