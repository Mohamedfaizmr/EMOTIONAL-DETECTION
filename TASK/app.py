

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

# Define questions for each level
level_1_questions = [
    "Have you canceled or avoided plans due to anxiety during the last month?",
    "How would you rate anxiety’s impact on your daily life on a scale of 1–5?",
    "Does anxiety ever impact your relationship with others?",
    "How often do you worry about how others perceive you? Have you had thoughts of self-harm during the past 30 days?",
    "How often do you avoid social situations due to feeling down?",
    "How frequently do you experience symptoms of depression, such as lack of appetite or inability to sleep?",
    "On a scale of 1–5, how much does depression interfere with your daily life?",
    "How often do you feel lonely?",
    "Are you worried about your current financial situation?",
    "How frequently do you procrastinate on a daily basis?",
    "Is there anything specific you would like to discuss?",
    "Do you think people can change their fundamental personality traits?",
    "Do you think time travel is theoretically possible?",
    "Do you believe in the concept of soulmates?",
    "If given the chance, would you restart your life?",
    "Do you believe in life after death?",
    "Do you believe that AI will overtake humans in the future?",
    "Is it possible for something to be both true and false at the same time?",
    "Is it ever possible to have complete and absolute certainty about anything?",
    "Can you have a thought without using language or symbols to represent it?",
]  # 20 questions for Level 1

level_2_questions = [
    "Is it possible to experience an emotion without being consciously aware of it?",
    "Is it possible for something to exist without having a location or position?",
    "Can you imagine a colour that has never been seen or described before?",
    "Can you have a thought without any influence from your personal experiences?",
    "Have you been feeling persistently sad or down lately?",
    "Have you lost interest in activities you used to enjoy?",
    "Do you feel hopeless about the future?",
    "Have you noticed changes in your appetite or sleep patterns?",
    "Do you often feel tired or lacking energy?",
    "Have you been withdrawing from social activities?",
    "Do you have difficulty concentrating on tasks?",
    "Do you feel like a burden to others?",
    "Have you had thoughts of self-harm or suicide?",
    "Do you feel like nothing is getting better, even when things seem positive?",
    "You are facing problems with making decisions",
    "You feel your life is sad, as there is no joy in your life anymore.",
    "You have lost interest in all things that were important to you once upon a time.",
    "You have been feeling guilty for everything you have done",
    "You have been very irritated and angry recently",
    "You have been feeling very fatigued",
    "You are feeling that everything you have done has been a failure",
    "You are having a lack of sleep",
    "You are having suicidal thoughts",
    "You have lost or gained weight without any diet programs.",
    "You are having a loss of appetite.",
]  # 25 questions for Level 2

level_3_questions = [
    "You are having trust issues with everyone around you.",
    "You are having trouble in all your relationships (home as well as professional)",
    "Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed",
    "Thoughts that you would be better off dead, or of hurting yourself",
    "If you checked off any problems, how difficult have these problems made it for you at work, home, or with other people?",
    "Do you often feel overwhelmed by stress?",
    "Do you find it difficult to trust others?",
    "Do you often experience mood swings?",
    "Do you feel anxious in social situations?",
    "Do you struggle to focus on tasks for extended periods?",
    "Do you often feel anxious in social situations?",
    "Have you ever had difficulty letting go of past relationships?",
    "Do you prefer staying in your comfort zone rather than taking risks?",
    "Do you often find it hard to express your emotions?",
    "Do you frequently overthink things?",
    "Are you easily affected by criticism?",
    "Do you find it hard to forgive others?",
    "Do you often feel overwhelmed by responsibilities?",
    "Are you generally a perfectionist?",
    "Do you have trouble saying 'no' to people?",
    "Do you feel overwhelmed by your emotions?",
    "Do you feel that your life lacks purpose or direction?",
]  # 25 questions for Level 3

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test/<int:level>', methods=['GET', 'POST'])
def test(level):
    if level == 1:
        questions = level_1_questions
    elif level == 2:
        questions = level_2_questions
    elif level == 3:
        questions = level_3_questions
    else:
        return "Invalid level", 400
    
    if request.method == 'POST':
        answers = request.form
        
        # Check if all questions are answered
        if len(answers) < len(questions):
            return render_template('index.html', questions=questions, level=level, error="Please answer all the questions before submitting!")
        
        total_questions = len(questions)
        yes_count = sum(1 for v in answers.values() if v == 'Yes')
        percentage = (yes_count / total_questions) * 100
        
        if percentage > 90:
            result = "Excellent"
        elif percentage > 40:
            result = "Good"
        else:
            result = "Bad"
        
        if result in ["Excellent", "Good"]:
            return render_template('result.html', result=result)
        elif level < 3:
            return redirect(url_for('test', level=level + 1))
        else:
            return render_template('result.html', result=result)
    
    return render_template('index.html', questions=questions, level=level, error=None)

if __name__ == '__main__':
    app.run(debug=True)