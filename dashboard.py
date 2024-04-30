import streamlit as st
from template.stress_predict import stress_pred
from template.chatbot import relate_chatbot
from template.sentiment_predict import sentiment_pred
# from template.relate_chatbot import relate_chatbot
# from homepage.email import send_mail
# from homepage.home import home

def main():
    st.set_page_config(page_title="Stress Prediction", page_icon=":brain:", layout="wide")
    st.sidebar.image("assets/modify square.png", use_column_width=True)
    
    st.sidebar.divider()
    
    menu_options = {
        "Tanya Moodify": relate_chatbot,
        "Deteksi Stress": stress_pred,
        "Konsultasi": sentiment_pred,
    }
    
    st.sidebar.info("Pilih opsi dari menu dibawah untuk melanjutkan ⬇️")
    menu_choice = st.sidebar.radio("Pilih menu", list(menu_options.keys()))
    
    st.sidebar.markdown("---")
    
    menu_options[menu_choice]()
        
if __name__ == "__main__":
    main()