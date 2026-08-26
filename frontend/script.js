let sessionId = "user_" + Date.now();


async function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value.trim();

    if (message === "") {
        return;
    }


    const chatBox = document.getElementById("chat-box");


    // Show user message

    const userMessage = document.createElement("div");

    userMessage.className = "user-message";

    userMessage.innerText = message;

    chatBox.appendChild(userMessage);


    input.value = "";


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/chat?message=${encodeURIComponent(message)}&session_id=${sessionId}`,
            {
                method: "POST"
            }
        );


        const data = await response.json();


        // Show bot response

        const botMessage = document.createElement("div");

        botMessage.className = "bot-message";

        botMessage.innerText = data.bot_response;

        chatBox.appendChild(botMessage);


        chatBox.scrollTop = chatBox.scrollHeight;


    } catch (error) {

        console.error(error);


        const errorMessage = document.createElement("div");

        errorMessage.className = "bot-message";

        errorMessage.innerText =
            "Sorry, I couldn't connect to the server.";

        chatBox.appendChild(errorMessage);
    }
}