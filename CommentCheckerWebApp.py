import streamlit as st
import requests  #The library to call your API


API_URL = "https://comments-filter-api-byteam2-csi.onrender.com/check-comment" 

st.set_page_config(page_title="Comment Moderator", page_icon="🛡️")
st.title("🛡️ Comment Moderator")
st.write("Enter a comment below to check it for spam and profanity using our ML models.")

user_input = st.text_area("Enter your comment:", height=150)

if st.button("Check Comment"):
    if user_input.strip() == "":
        st.warning("Please enter a comment to check.")
    else:
        with st.spinner("Analyzing comment..."):
            try:
                #yahan hum define kar rahe hain apna payload us json format mein jisme hume request bhejni hai
                payload = {"text": user_input}
                
                #yahan hum post request bhej rahe hain apni fast API ko
                response = requests.post(API_URL, json=payload, timeout=10)
                
                #Checking for a successful response
                if response.status_code == 200:
                    #Get the JSON data from the response
                    data = response.json()
                    
                    st.divider()
                    st.subheader("Analysis Results:")
                    
                    #showing the results
                    spam_data = data['spam_check']
                    spam_prob = spam_data['confidence']
                    if spam_data['is_spam']:
                        st.error(f"Spam Check: Flagged as SPAM (Confidence: {spam_prob*100:.2f}%)")
                    else:
                        st.success(f"Spam Check: Not Spam (Spam Probability: {spam_prob*100:.2f}%)")
                    
                    
                    prof_data = data['profanity_check']
                    prof_prob = prof_data['confidence']
                    if prof_data['is_profane']:
                        st.error(f"Profanity Check: Flagged as PROFANE (Confidence: {prof_prob*100:.2f}%)")
                    else:
                        st.success(f"Profanity Check: Not Profane (Profanity Probability: {prof_prob*100:.2f}%)")

                else:
                    # Show an error if the API is down or has a problem
                    st.error(f"Error: Could not get a response from the API (Status Code: {response.status_code})")

            except requests.exceptions.RequestException as e:
                # Show an error if the request fails (e.g., no internet, API URL is wrong)
                st.error(f"Error: Could not connect to the API. {e}")