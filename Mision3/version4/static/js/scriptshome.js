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

  sendBtn.addEventListener("click", async (e)=>{ 
   e.preventDefault();
   const text = messageInput.value.trim();
    if (!text) return;
    messages.innerHTML += `<p><strong>Tú:</strong> ${text}</p>`;
    messageInput.value = "";
    
    const response =await  fetch("/chat",{
    	method:"POST",
    	headers:{"Content-Type": "application/x-www-form-urlencoded"},
    	body:`message=${encodeURIComponent(text)}`
        
    });
    
    const data = await response.json();
    messages.innerHTML+=`<div class="msg bot"><strong>Bot:</strong> ${data.response}</div>`;
    messages.scrollTop = messages.scrollHeight;
    })

