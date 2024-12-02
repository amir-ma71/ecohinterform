import streamlit as st

# تنظیمات Mini App
st.set_page_config(page_title="Mini App Telegram", layout="centered")

# نمایش فرم اطلاعات
st.title("فرم اطلاعات برای مینی‌اپ تلگرام")
name = st.text_input("نام:")
email = st.text_input("ایمیل:")
age = st.number_input("سن:", min_value=0, max_value=100, step=1)
feedback = st.text_area("بازخورد:")
city = st.text_input("شهر:")

# دکمه ارسال
if st.button("ارسال"):
    # جمع‌آوری اطلاعات
    data = {
        "نام": name,
        "ایمیل": email,
        "سن": age,
        "بازخورد": feedback,
        "شهر": city
    }

    # نمایش نتیجه به کاربر
    st.success("اطلاعات شما با موفقیت ثبت شد!")

    # ارسال داده به تلگرام با WebApp
    st.write("در حال ارسال داده به تلگرام...")
    st.write(data)
