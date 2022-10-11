import streamlit as st
import pickle
import numpy as np

loaded_model = pickle.load(open('phishing.pkl', 'rb'))

def predict_forest(Url):
    X_predict = []
    X_predict.append(str(Url))
    prediction = loaded_model.predict(X_predict)
    ##input=np.array([[Url]]).astype(np.float64)
    ##prediction = loaded_model.predict(input)
    ##pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return (prediction)

def main():
    st.title("# Check whether a website is safe to visit")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Malicious website detection </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Url = st.text_input("Enter the name or the url of the website you need to check")

    if st.button("Check"):
        output=predict_forest(Url)
        st.success('That website  is {}'.format(output))

        if output == 'bad':
            if output == 'bad':
                st.write = ("This is a Phishing Site")
            else:
                st.write = ("This is not a Phishing Site")
            ##st.markdown(danger_html,unsafe_allow_html=True)
        ##else:
           ##st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()