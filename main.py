import time

def interview_buddy_simulator():
    """
    Simulates a basic offline AI interview.
    """
    print("Merhaba! Ben Interview Buddy. Mülakat simülasyonumuza hoş geldin.")
    print("Sana bazı sorular soracağım. Lütfen cevaplarını yazıp Enter'a bas.")
    print("-" * 40)
    time.sleep(1)

    # Predefined interview questions, mimicking the simulator's question bank
    questions = [
        "Kendinden bahseder misin?", # Tell me about yourself?
        "Neden bu pozisyona başvurdun?", # Why did you apply for this position?
        "Güçlü yönlerin nelerdir?", # What are your strengths?
        "Zayıf yönlerin nelerdir?", # What are your weaknesses?
        "5 yıl sonra kendini nerede görüyorsun?", # Where do you see yourself in 5 years?
    ]

    # Simple feedback mechanism (mock AI evaluation based on keywords)
    feedback_phrases = {
        "iyi": "Bu harika bir nokta. Kendine güvenin takdire şayan.", # That's a great point. Your confidence is admirable.
        "gelişim": "Gelişim alanlarını fark etmen olgunluğunu gösterir.", # Recognizing areas for improvement shows maturity.
        "hedef": "Belirgin hedeflere sahip olman vizyonunu ortaya koyuyor.", # Having clear goals reveals your vision.
        "genel": "Anladım. Cevabın için teşekkürler.", # Understood. Thanks for your answer.
    }

    # Simulate the interview process
    for i, question in enumerate(questions):
        print(f"\nInterview Buddy: Soru {i+1}: {question}")
        user_answer = input("Sen: ").strip().lower() # Get user input

        # --- Core "AI" logic for offline simulation ---
        # This is a simplified, rule-based "AI" for demonstration purposes.
        # In a real "Interview Buddy" system, this would involve more advanced
        # NLP, sentiment analysis, or a local machine learning model.
        feedback = feedback_phrases["genel"] # Default feedback

        if "güçlü" in question and ("beceri" in user_answer or "deneyim" in user_answer or "başarı" in user_answer):
            feedback = feedback_phrases["iyi"]
        elif "zayıf" in question and ("öğrenme" in user_answer or "gelişim" in user_answer or "çalışıyorum" in user_answer):
            feedback = feedback_phrases["gelişim"]
        elif "yıl sonra" in question and ("hedef" in user_answer or "kariyer" in user_answer or "uzmanlaşmak" in user_answer):
            feedback = feedback_phrases["hedef"]
        # --- End of "AI" logic ---

        print(f"Interview Buddy: {feedback}")
        time.sleep(1.5) # Pause for readability

    print("\nInterview Buddy: Mülakat simülasyonumuz sona erdi. Katılımın için teşekkürler!")
    print("Umarım bu pratik sana yardımcı olmuştur. Başarılar dilerim!")

if __name__ == "__main__":
    interview_buddy_simulator()
