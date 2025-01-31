# # # # import streamlit as st
# # # # import re
# # # # import pickle
# # # # import logging
# # # # import numpy as np

# # # # # Configure logging
# # # # logging.basicConfig(level=logging.INFO)

# # # # def load_model(file_path):
# # # #     try:
# # # #         with open(file_path, 'rb') as file:
# # # #             return pickle.load(file)
# # # #     except Exception as e:
# # # #         logging.error(f"Error loading model {file_path}: {e}")
# # # #         return None

# # # # # Load ML models
# # # # spam_tfidf_vectorizer = load_model("feature_extraction_spam.pkl")
# # # # spam_classifier = load_model("svm_spam.pkl")

# # # # class PhishingDetector:
# # # #     def __init__(self):
# # # #         self.suspicious_tlds = ['.xyz', '.club', '.top', '.work', '.info', '.biz', 
# # # #                               '.tk', '.ml', '.ga', '.cf', '.wap', '.loan']
    
# # # #     def contains_urls(self, text):
# # # #         return bool(re.findall(r'https?://\S+', text))
    
# # # #     def is_suspicious_url(self, url):
# # # #         return any(url.lower().endswith(tld) for tld in self.suspicious_tlds)
    
# # # #     def detect(self, text):
# # # #         if len(text) < 60:
# # # #             return "Insufficient Text"
            
# # # #         urls = re.findall(r'https?://\S+', text)
# # # #         if urls:
# # # #             suspicious_urls = [url for url in urls if self.is_suspicious_url(url)]
# # # #             if suspicious_urls:
# # # #                 return "Phishing", suspicious_urls
# # # #             return "Phishing", urls
# # # #         return "Not Phishing", []

# # # # class SpamDetector:
# # # #     def __init__(self):
# # # #         self.spam_keywords = [
# # # #             "sms", "reply", "end", "sptv", "txt", "stop", "cancel", 
# # # #             "unsubscribe", "limited time", "offer", "urgent"
# # # #         ]
        
# # # #     def ml_spam_detection(self, text):
# # # #         if spam_tfidf_vectorizer and spam_classifier:
# # # #             try:
# # # #                 vectorized_text = spam_tfidf_vectorizer.transform([text])
# # # #                 return spam_classifier.predict(vectorized_text)[0] == 1
# # # #             except Exception as e:
# # # #                 logging.error(f"ML Spam detection error: {e}")
# # # #         return False
    
# # # #     def contains_spam_keywords(self, text):
# # # #         return sum(keyword.lower() in text.lower() for keyword in self.spam_keywords)
    
# # # #     def detect(self, text):
# # # #         if len(text) < 60:
# # # #             return "Insufficient Text"
            
# # # #         spam_score = self.contains_spam_keywords(text)
# # # #         ml_result = self.ml_spam_detection(text)
        
# # # #         if spam_score > 1 or ml_result:
# # # #             return "Spam"
# # # #         return "Not Spam"

# # # # def main():
# # # #     st.title("🛡️ Message Security Classifier")
    
# # # #     # Navigation
# # # #     page = st.sidebar.radio("Select Detection Type", ["Phishing Detection", "Spam Detection"])
    
# # # #     # Input text area
# # # #     message_input = st.text_area("Enter message content (minimum 60 characters)", height=200)
    
# # # #     if page == "Phishing Detection":
# # # #         st.header("Phishing Detection")
# # # #         if st.button("Check for Phishing"):
# # # #             if message_input:
# # # #                 detector = PhishingDetector()
# # # #                 result, urls = detector.detect(message_input)
                
# # # #                 if result == "Insufficient Text":
# # # #                     st.warning("Please enter at least 60 characters")
# # # #                 elif result == "Phishing":
# # # #                     st.error("🚨 PHISHING DETECTED!")
# # # #                     st.warning(f"Suspicious URLs found: {', '.join(urls)}")
# # # #                 else:
# # # #                     st.success("✅ No phishing detected")
    
# # # #     else:  # Spam Detection
# # # #         st.header("Spam Detection")
# # # #         if st.button("Check for Spam"):
# # # #             if message_input:
# # # #                 detector = SpamDetector()
# # # #                 result = detector.detect(message_input)
                
# # # #                 if result == "Insufficient Text":
# # # #                     st.warning("Please enter at least 60 characters")
# # # #                 elif result == "Spam":
# # # #                     st.warning("🚩 SPAM DETECTED")
# # # #                 else:
# # # #                     st.success("✅ Not spam")

# # # # if __name__ == "__main__":
# # # #     main()


# # # import streamlit as st
# # # import re
# # # import pickle
# # # import logging
# # # import numpy as np

# # # logging.basicConfig(level=logging.INFO)

# # # def load_model(file_path):
# # #     try:
# # #         with open(file_path, 'rb') as file:
# # #             return pickle.load(file)
# # #     except Exception as e:
# # #         logging.error(f"Error loading model {file_path}: {e}")
# # #         st.error(f"Failed to load model: {file_path}")
# # #         return None

# # # # Validate models on load
# # # spam_tfidf_vectorizer = load_model("feature_extraction_spam.pkl")
# # # spam_classifier = load_model("svm_spam.pkl")

# # # class PhishingDetector:
# # #     def __init__(self):
# # #         self.suspicious_tlds = ['.xyz', '.club', '.top', '.work', '.info', '.biz', 
# # #                               '.tk', '.ml', '.ga', '.cf', '.wap', '.loan']
    
# # #     def contains_urls(self, text):
# # #         if not isinstance(text, str):
# # #             return False
# # #         return bool(re.findall(r'https?://\S+', text))
    
# # #     def is_suspicious_url(self, url):
# # #         if not isinstance(url, str):
# # #             return False
# # #         return any(url.lower().endswith(tld) for tld in self.suspicious_tlds)
    
# # #     def detect(self, text):
# # #         if not isinstance(text, str):
# # #             return "Invalid Input", []
        
# # #         text = text.strip()
# # #         if len(text) < 60:
# # #             return "Insufficient Text", []
            
# # #         urls = re.findall(r'https?://\S+', text)
# # #         if urls:
# # #             suspicious_urls = [url for url in urls if self.is_suspicious_url(url)]
# # #             if suspicious_urls:
# # #                 return "Phishing", suspicious_urls
# # #             return "Phishing", urls
# # #         return "Not Phishing", []

# # # class SpamDetector:
# # #     def __init__(self):
# # #         self.spam_keywords = [
# # #             "sms", "reply", "end", "sptv", "txt", "stop", "cancel", 
# # #             "unsubscribe", "limited time", "offer", "urgent"
# # #         ]
        
# # #     def ml_spam_detection(self, text):
# # #         if not (spam_tfidf_vectorizer and spam_classifier):
# # #             logging.error("ML models not loaded properly")
# # #             return False
            
# # #         try:
# # #             vectorized_text = spam_tfidf_vectorizer.transform([text])
# # #             return spam_classifier.predict(vectorized_text)[0] == 1
# # #         except Exception as e:
# # #             logging.error(f"ML Spam detection error: {e}")
# # #             return False
    
# # #     def contains_spam_keywords(self, text):
# # #         if not isinstance(text, str):
# # #             return 0
# # #         return sum(keyword.lower() in text.lower() for keyword in self.spam_keywords)
    
# # #     def detect(self, text):
# # #         if not isinstance(text, str):
# # #             return "Invalid Input"
            
# # #         text = text.strip()
# # #         if len(text) < 60:
# # #             return "Insufficient Text"
            
# # #         spam_score = self.contains_spam_keywords(text)
# # #         ml_result = self.ml_spam_detection(text)
        
# # #         if spam_score > 1 or ml_result:
# # #             return "Spam"
# # #         return "Not Spam"

# # # def main():
# # #     st.set_page_config(page_title="Message Security Classifier", layout="wide")
# # #     st.title("🛡️ Message Security Classifier")
    
# # #     page = st.sidebar.radio("Select Detection Type", ["Phishing Detection", "Spam Detection"])
    
# # #     # Input validation before processing
# # #     message_input = st.text_area(
# # #         "Enter message content (minimum 60 characters)", 
# # #         height=200,
# # #         key="message_input"
# # #     )
    
# # #     char_count = len(message_input.strip())
# # #     st.write(f"Character count: {char_count}/60")
    
# # #     if page == "Phishing Detection":
# # #         st.header("Phishing Detection")
# # #         if st.button("Check for Phishing"):
# # #             if not message_input:
# # #                 st.error("Please enter some text")
# # #             elif char_count < 60:
# # #                 st.warning("⚠️ Please enter at least 60 characters")
# # #             else:
# # #                 try:
# # #                     detector = PhishingDetector()
# # #                     result, urls = detector.detect(message_input)
                    
# # #                     if result == "Insufficient Text":
# # #                         st.warning("⚠️ Please enter at least 60 characters")
# # #                     elif result == "Invalid Input":
# # #                         st.error("Invalid input detected")
# # #                     elif result == "Phishing":
# # #                         st.error("🚨 PHISHING DETECTED!")
# # #                         if urls:
# # #                             st.warning("Suspicious URLs found:")
# # #                             for url in urls:
# # #                                 st.warning(f"- {url}")
# # #                     else:
# # #                         st.success("✅ No phishing detected")
# # #                 except Exception as e:
# # #                     logging.error(f"Phishing detection error: {e}")
# # #                     st.error("An error occurred during detection")
    
# # #     else:  # Spam Detection
# # #         st.header("Spam Detection")
# # #         if st.button("Check for Spam"):
# # #             if not message_input:
# # #                 st.error("Please enter some text")
# # #             elif char_count < 60:
# # #                 st.warning("⚠️ Please enter at least 60 characters")
# # #             else:
# # #                 try:
# # #                     detector = SpamDetector()
# # #                     result = detector.detect(message_input)
                    
# # #                     if result == "Insufficient Text":
# # #                         st.warning("⚠️ Please enter at least 60 characters")
# # #                     elif result == "Invalid Input":
# # #                         st.error("Invalid input detected")
# # #                     elif result == "Spam":
# # #                         st.warning("🚩 SPAM DETECTED")
# # #                     else:
# # #                         st.success("✅ Not spam")
# # #                 except Exception as e:
# # #                     logging.error(f"Spam detection error: {e}")
# # #                     st.error("An error occurred during detection")

# # # if __name__ == "__main__":
# # #     main()


# # import streamlit as st
# # import re
# # import pickle
# # import logging
# # import numpy as np

# # logging.basicConfig(level=logging.INFO)

# # def load_model(file_path):
# #     try:
# #         with open(file_path, 'rb') as file:
# #             return pickle.load(file)
# #     except Exception as e:
# #         logging.error(f"Error loading model {file_path}: {e}")
# #         return None

# # # Load ML models
# # with open("feature_extraction_spam.pkl", 'rb') as file:
# #     spam_tfidf_vectorizer = pickle.load(file)

# # with open("svm_spam.pkl", 'rb') as file:
# #     spam_classifier = pickle.load(file)

# # with open("tfidf_vectorize_phishing.pkl", 'rb') as file:
# #     phishing_tfidf_vectorizer = pickle.load(file)

# # with open("lr_classifier_phishing.pkl", 'rb') as file:
# #     phishing_classifier = pickle.load(file)

# # class SpamDetector:
# #     def __init__(self):
# #         self.spam_keywords = [
# #             "sms", "reply", "end", "sptv", "txt", "stop", "cancel", 
# #             "unsubscribe", "limited time", "offer", "urgent"
# #         ]
# #         self.spam_threshold = 2  # Adjusted threshold
    
# #     def ml_spam_detection(self, text):
# #         if spam_tfidf_vectorizer and spam_classifier:
# #             try:
# #                 vectorized_text = spam_tfidf_vectorizer.transform([text])
# #                 prediction = spam_classifier.predict(vectorized_text)[0]
# #                 logging.info(f"ML Model Prediction: {prediction}")
# #                 return prediction == 1
# #             except Exception as e:
# #                 logging.error(f"ML Spam detection error: {e}")
# #         return False
    
# #     def contains_spam_keywords(self, text):
# #         return sum(keyword.lower() in text.lower() for keyword in self.spam_keywords)
    
# #     def detect(self, text):
# #         if not isinstance(text, str) or len(text.strip()) < 60:
# #             return "Insufficient Text"
        
# #         spam_score = self.contains_spam_keywords(text)
# #         ml_result = self.ml_spam_detection(text)
        
# #         logging.info(f"Spam Score: {spam_score}, ML Result: {ml_result}")
        
# #         if spam_score >= self.spam_threshold or ml_result:
# #             return "Spam"
# #         return "Not Spam"

# # def main():
# #     st.set_page_config(page_title="Message Security Classifier", layout="wide")
# #     st.title("🛡️ Message Security Classifier")
    
# #     page = st.sidebar.radio("Select Detection Type", ["Spam Detection"])
# #     message_input = st.text_area("Enter message content (minimum 60 characters)", height=200)
    
# #     char_count = len(message_input.strip())
# #     st.write(f"Character count: {char_count}/60")
    
# #     if page == "Spam Detection":
# #         st.header("Spam Detection")
# #         if st.button("Check for Spam"):
# #             if char_count < 60:
# #                 st.warning("⚠️ Please enter at least 60 characters")
# #             else:
# #                 detector = SpamDetector()
# #                 result = detector.detect(message_input)
                
# #                 if result == "Spam":
# #                     st.warning("🚩 SPAM DETECTED")
# #                 else:
# #                     st.success("✅ Not spam")

# # if __name__ == "__main__":
# #     main()



# import streamlit as st
# import re
# import pickle
# import logging
# import numpy as np

# logging.basicConfig(level=logging.INFO)

# def load_model(file_path):
#     try:
#         with open(file_path, 'rb') as file:
#             return pickle.load(file)
#     except Exception as e:
#         logging.error(f"Error loading model {file_path}: {e}")
#         return None

# # Load ML models
# with open("feature_extraction_spam.pkl", 'rb') as file:
#     spam_tfidf_vectorizer = pickle.load(file)

# with open("svm_spam.pkl", 'rb') as file:
#     spam_classifier = pickle.load(file)

# with open("tfidf_vectorize_phishing.pkl", 'rb') as file:
#     phishing_tfidf_vectorizer = pickle.load(file)

# with open("lr_classifier_phishing.pkl", 'rb') as file:
#     phishing_classifier = pickle.load(file)

# class SpamDetector:
#     def __init__(self):
#         self.spam_keywords = [
#             "sms", "reply", "end", "sptv", "txt", "stop", "cancel", 
#             "unsubscribe", "limited time", "offer", "urgent"
#         ]
#         self.spam_threshold = 2  
    
#     def ml_spam_detection(self, text):
#         if spam_tfidf_vectorizer and spam_classifier:
#             try:
#                 vectorized_text = spam_tfidf_vectorizer.transform([text])
#                 prediction = spam_classifier.predict(vectorized_text)[0]
#                 logging.info(f"ML Model Prediction: {prediction}")
#                 return prediction == 1
#             except Exception as e:
#                 logging.error(f"ML Spam detection error: {e}")
#         return False
    
#     def contains_spam_keywords(self, text):
#         return sum(keyword.lower() in text.lower() for keyword in self.spam_keywords)
    
#     def detect(self, text):
#         if not isinstance(text, str) or len(text.strip()) < 60:
#             return "Insufficient Text"
        
#         spam_score = self.contains_spam_keywords(text)
#         ml_result = self.ml_spam_detection(text)
        
#         logging.info(f"Spam Score: {spam_score}, ML Result: {ml_result}")
        
#         if spam_score >= self.spam_threshold or ml_result:
#             return "Spam"
#         return "Not Spam"

# class PhishingDetector:
#     def detect(self, text):
#         if not isinstance(text, str) or len(text.strip()) < 60:
#             return "Insufficient Text"
        
#         try:
#             vectorized_text = phishing_tfidf_vectorizer.transform([text])
#             prediction = phishing_classifier.predict(vectorized_text)[0]
#             logging.info(f"Phishing Model Prediction: {prediction}")
#             return "Phishing" if prediction == 1 else "Not Phishing"
#         except Exception as e:
#             logging.error(f"Phishing detection error: {e}")
#             return "Error"

# def main():
#     st.set_page_config(page_title="Message Security Classifier", layout="wide")
#     st.title("🛡️ Message Security Classifier")
    
#     page = st.sidebar.radio("Select Detection Type", ["Spam Detection", "Phishing Detection"])
#     message_input = st.text_area("Enter message content (minimum 60 characters)", height=200)
    
#     char_count = len(message_input.strip())
#     st.write(f"Character count: {char_count}/60")
    
#     if page == "Spam Detection":
#         st.header("Spam Detection")
#         if st.button("Check for Spam"):
#             if char_count < 60:
#                 st.warning("⚠️ Please enter at least 60 characters")
#             else:
#                 detector = SpamDetector()
#                 result = detector.detect(message_input)
                
#                 if result == "Spam":
#                     st.warning("🚩 SPAM DETECTED")
#                 else:
#                     st.success("✅ Not spam")
    
#     elif page == "Phishing Detection":
#         st.header("Phishing Detection")
#         if st.button("Check for Phishing"):
#             if char_count < 60:
#                 st.warning("⚠️ Please enter at least 60 characters")
#             else:
#                 detector = PhishingDetector()
#                 result = detector.detect(message_input)
                
#                 if result == "Phishing":
#                     st.warning("🚨 PHISHING DETECTED")
#                 else:
#                     st.success("✅ Not phishing")

# if __name__ == "__main__":
#     main()



import streamlit as st
import re
import pickle
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)

def load_model(file_path):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        logging.error(f"Error loading model {file_path}: {e}")
        return None

# Load ML models
with open("feature_extraction_spam.pkl", 'rb') as file:
    spam_tfidf_vectorizer = pickle.load(file)

with open("svm_spam.pkl", 'rb') as file:
    spam_classifier = pickle.load(file)

with open("tfidf_vectorize_phishing.pkl", 'rb') as file:
    phishing_tfidf_vectorizer = pickle.load(file)

with open("lr_classifier_phishing.pkl", 'rb') as file:
    phishing_classifier = pickle.load(file)

class SpamDetector:
    def __init__(self):
        self.spam_keywords = [
            "sms", "reply", "end", "sptv", "txt", "stop", "cancel", 
            "unsubscribe", "limited time", "offer", "urgent"
        ]
        self.spam_threshold = 2  
    
    def ml_spam_detection(self, text):
        if spam_tfidf_vectorizer and spam_classifier:
            try:
                vectorized_text = spam_tfidf_vectorizer.transform([text])
                prediction = spam_classifier.predict(vectorized_text)[0]
                logging.info(f"ML Model Prediction: {prediction}")
                return prediction == 1
            except Exception as e:
                logging.error(f"ML Spam detection error: {e}")
        return False
    
    def contains_spam_keywords(self, text):
        return sum(keyword.lower() in text.lower() for keyword in self.spam_keywords)
    
    def detect(self, text):
        if not isinstance(text, str) or len(text.strip()) < 60:
            return "Insufficient Text"
        
        spam_score = self.contains_spam_keywords(text)
        ml_result = self.ml_spam_detection(text)
        
        logging.info(f"Spam Score: {spam_score}, ML Result: {ml_result}")
        
        if spam_score >= self.spam_threshold or ml_result:
            return "Spam"
        return "Not Spam"

class PhishingDetector:
    def detect(self, text):
        if not isinstance(text, str) or len(text.strip()) < 60:
            return "Insufficient Text"
        
        if re.search(r'https?://\S+', text):
            return "Phishing"
        
        try:
            vectorized_text = phishing_tfidf_vectorizer.transform([text])
            prediction = phishing_classifier.predict(vectorized_text)[0]
            logging.info(f"Phishing Model Prediction: {prediction}")
            return "Phishing" if prediction == 1 else "Not Phishing"
        except Exception as e:
            logging.error(f"Phishing detection error: {e}")
            return "Error"

def main():
    st.set_page_config(page_title="Message Security Classifier", layout="wide")
    st.title("🛡️ Message Security Classifier")
    
    page = st.sidebar.radio("Select Detection Type", ["Spam Detection", "Phishing Detection"])
    message_input = st.text_area("Enter message content (minimum 60 characters)", height=200)
    
    char_count = len(message_input.strip())
    st.write(f"Character count: {char_count}/60")
    
    if page == "Spam Detection":
        st.header("Spam Detection")
        if st.button("Check for Spam"):
            if char_count < 60:
                st.warning("⚠️ Please enter at least 60 characters")
            else:
                detector = SpamDetector()
                result = detector.detect(message_input)
                
                if result == "Spam":
                    st.warning("🚩 SPAM DETECTED")
                else:
                    st.success("✅ Not spam")
    
    elif page == "Phishing Detection":
        st.header("Phishing Detection")
        if st.button("Check for Phishing"):
            if char_count < 60:
                st.warning("⚠️ Please enter at least 60 characters")
            else:
                detector = PhishingDetector()
                result = detector.detect(message_input)
                
                if result == "Phishing":
                    st.warning("🚨 PHISHING DETECTED")
                else:
                    st.success("✅ Not phishing")

if __name__ == "__main__":
    main()
