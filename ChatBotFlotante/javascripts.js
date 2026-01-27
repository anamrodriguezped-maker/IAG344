  const chatButton = document.getElementById("chat-button");
  const chatBox = document.getElementById("chat-box");
  const closeChat = document.getElementById("close-chat");
  const sendBtn = document.getElementById("send");
  const messageInput = document.getElementById("message");
  const messages = document.getElementById("chat-messages");

  chatButton.addEventListener("click", () => {
    chatBox.style.display = "flex";
  });

  closeChat.addEventListener("click", () => {
    chatBox.style.display = "none";
  });

  sendBtn.addEventListener("click", sendMessage);

  function sendMessage() {
    const text = messageInput.value.trim();
    if (text === "") return;

    messages.innerHTML += `<p><strong>Tú:</strong> ${text}</p>`;
    messageInput.value = "";
    messages.scrollTop = messages.scrollHeight;

    // Respuesta simulada
    setTimeout(() => {
      messages.innerHTML += `<p><strong>Bot:</strong> Te leo 💖</p>`;
      messages.scrollTop = messages.scrollHeight;
    }, 600);
  }