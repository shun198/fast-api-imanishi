import streamlit as st
import random
import requests
import json


page = st.sidebar.selectbox("Choose your page", ["users", "rooms"])

if page == "users":
    st.title("APIテスト画面(ユーザ)")
    with st.form(key="user"):
        user_id: int = random.randint(0, 100)
        username: str = st.text_input("ユーザ名", max_chars=20)
        data = {
            "user_id": user_id,
            "username": username
        }
        submit_button = st.form_submit_button(label="リクエスト送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url = "http://127.0.0.1:8000/users"
        response = requests.post(
            url,
            data=json.dumps(data),
        )
        st.write(response.status_code)
        st.json(response.json())
elif page == "rooms":
    st.title("APIテスト画面(会議室)")
    with st.form(key="room"):
        room_id: int = random.randint(0, 10)
        room_name: str = st.text_input("会議室名", max_chars=20)
        capacity: int = st.number_input("定員", step=1)
        data = {
            "room_id": room_id,
            "room_name": room_name,
            "capacity": capacity
        }
        submit_button = st.form_submit_button(label="リクエスト送信")

    if submit_button:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url = "http://127.0.0.1:8000/rooms"
        response = requests.post(
            url,
            data=json.dumps(data),
        )
        st.write(response.status_code)
        st.json(response.json())