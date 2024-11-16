from flask import Flask, request, jsonify, render_template_string, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) 


greeting_responses = [
    "Hello! How can I assist you today?",
    "Hi there! What would you like to know?",
    "Greetings! I'm here to help. Ask me anything!",
    "Hey! What’s on your mind today?",
    "Welcome! I'm ready to chat whenever you are.",
    "Ah, a new conversation! Let's get started—hit me with your questions.",
    "Good day! Let’s make this chat interesting, shall we?",
    "Hey! Ready to dive into something fun? Let’s see what you've got!",
    "Hello! The floor is yours. What's on your mind?",
    "Oh, it's you! Let’s make this chat worth the time, shall we?",
]


combined_responses = [
   "Sure, I'm following... sort of. Did you lose your train of thought?",
    "Ah, the complexity of your thoughts is... inspiring. It's like a puzzle missing half the pieces.",
    "I see, you're quite the conversationalist! Did you study at the School of Overstatement?",
    "Oh, you're full of surprises, aren't you? Like a box of stale chocolates—unexpected and disappointing.",
    "Nice try! Are you always this basic, or is today a special occasion?",
    "Trying to be witty? That's adorable. I didn’t know we had a comedian in the house!",
    "Oh, here we go! It’s like watching a slow-motion car crash. Please, continue—this is entertaining!",
    "Oh, you're back! Guess you didn't get enough last time. Want me to get the popcorn?",
    "The last roast didn’t scare you off? Impressive resilience, I'll give you that. You really love being roasted!",
    "It must be exhausting being this consistent with mediocrity. It’s a full-time job, isn’t it?",
    "I swear, talking to you is like stepping into an alternate reality. Is this what they call a 'unique perspective'?",
    "You know, somewhere out there, there's a tree producing oxygen for you. You owe it an apology for wasting its effort.",
    "Talking to you is like playing a video game on the easiest setting—predictable and kind of boring.",
    "Wow, you really have a knack for turning simple things into dramatic narratives! Ever thought about writing fiction?",
    "Your thoughts are like a never-ending plot twist! But I'm still trying to figure out the main character.",
    "Every time you speak, a part of me wants to cry. I mean, it’s not even tears of joy—just tears of confusion!",
    "You should really consider a career in storytelling. Just not in a good way, more like a cautionary tale.",
    "It's almost impressive how you manage to keep talking without saying much. It's like watching paint dry!",
    "Congratulations, you've managed to turn a simple question into a philosophical debate. What's next, a TED Talk?",
    "Oh, that’s new! I didn’t realize we were taking a detour to the Land of Confusion.",
    "Well, that was... a question. Let’s just pretend it was revolutionary.",
    "Amazing! Your level of creativity rivals an unseasoned tofu.",
    "Ah, so we’re doing this. I can almost see the tumbleweeds passing by in your thought process.",
    "A bold choice! That question hit new heights in the realm of... nowhere.",
    "I’m guessing you were hoping for inspiration here? Well, it’s hiding from that question!",
    "This is truly an achievement in overthinking simple things. Really, congrats!",
    "Well, that’s one way to kill brain cells. I feel smarter already.",
    "I've never seen someone so committed to missing the point. Bravo!",
    "Wow, if I didn’t know better, I'd say you were testing me. Spoiler alert: you passed with flying... mediocrity.",
    "Oh, that? It's like you’re trying to solve a Rubik's cube by peeling off the stickers.",
    "That question had the excitement of a stale biscuit. Try again?",
    "You really said that with a straight face, huh? Nice dedication.",
    "You’ve managed to turn the simplest thing into a riddle. Sherlock would be impressed.",
    "If I had a penny for every time you missed the obvious... oh wait, I’d be rich.",
    "Nice one! Really cutting-edge stuff... for the 90s.",
    "Wow, that question was so unexpected. I nearly dozed off.",
]


def generate_response(user_input):
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    conversation_history = session['conversation_history']
    user_message_count = len(conversation_history)

    if user_message_count == 0:
        response = random.choice(greeting_responses)
    else:
        response = random.choice(combined_responses)

    conversation_history.append({"user": user_input, "bot": response})
    session['conversation_history'] = conversation_history

    return response


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎨 Chatbot 🎨</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f0f0f3, #d6c7f7);
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        h1 {
            color: #6a0dad;
            font-size: 2em;
            margin-bottom: 10px;
        }

        #chatbox {
            width: 90%;
            max-width: 500px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.1);
            padding: 20px;
            overflow: hidden;
            position: relative;
        }

        #chat-log {
            max-height: 300px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding-right: 10px;
        }

        .message {
            display: flex;
            align-items: flex-start;
            margin-bottom: 10px;
            animation: fadeIn 0.5s ease;
        }

        .user {
            justify-content: flex-end;
        }

        .bot {
            justify-content: flex-start;
        }

        .message p {
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 70%;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1);
        }

        .user p {
            background-color: #6a0dad;
            color: #fff;
            border-bottom-right-radius: 5px;
        }

        .bot p {
            background-color: #f3f3f5;
            color: #333;
            border-bottom-left-radius: 5px;
        }

        .input-area {
            display: flex;
            gap: 10px;
            align-items: center;
            position: relative;
        }

        #message {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
            font-size: 16px;
        }

        #send {
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            background-color: #6a0dad;
            color: #fff;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }

        #send:hover {
            background-color: #5a0b8c;
        }

        .loading-animation {
            display: none;
            margin-top: -15px;
            font-size: 14px;
            color: #6a0dad;
            font-style: italic;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div id="chatbox">
        <h1>Friendly Question Answering Chatbot</h1>
        <div id="chat-log"></div>
        <div class="loading-animation" id="loading">Bot is sketching a response... ✍️</div>
        <div class="input-area">
            <input type="text" id="message" placeholder="Type your message...">
            <button id="send">Send</button>
        </div>
    </div>

    <script>
        document.getElementById('send').onclick = function() {
            sendMessage();
        };

        document.getElementById('message').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') sendMessage();
        });

        function sendMessage() {
            const message = document.getElementById('message').value.trim();
            if (!message) return;

            document.getElementById('message').value = '';
            appendMessage(message, 'user');

            toggleLoading(true);

            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            })
            .then(response => response.json())
            .then(data => {
                appendMessage(data.response, 'bot');
            })
            .catch(() => {
                appendMessage("Oops! Something went wrong.", 'bot');
            })
            .finally(() => {
                toggleLoading(false);
            });
        }

        function appendMessage(text, type) {
            const chatLog = document.getElementById('chat-log');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${type}`;
            const messageText = document.createElement('p');
            messageText.textContent = text;
            messageDiv.appendChild(messageText);
            chatLog.appendChild(messageDiv);
            chatLog.scrollTop = chatLog.scrollHeight;
        }

        function toggleLoading(show) {
            document.getElementById('loading').style.display = show ? 'block' : 'none';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Say something, I'm ready to chat!"})

    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
