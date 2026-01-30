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

document.getElementById("register-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const usuario = document.getElementById("reg-usuario").value;
    const correo = document.getElementById("reg-correo").value;
    const password = document.getElementById("reg-password").value;
    const password2 = document.getElementById("reg-password2").value;

    if (password !== password2) {
        alert("Las contraseñas no coinciden ❌");
        return;
    }

    const usuarioData = { usuario, correo, password };
    localStorage.setItem("usuario", JSON.stringify(usuarioData));

    alert("Registro exitoso ✅");
});

// LOGIN
document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const usuarioLogin = document.getElementById("login-usuario").value;
    const passwordLogin = document.getElementById("login-password").value;

    const data = JSON.parse(localStorage.getItem("usuario"));

    if (!data) {
        alert("No hay usuarios registrados");
        return;
    }

    if (usuarioLogin === data.usuario && passwordLogin === data.password) {
        alert("Inicio de sesión exitoso 😎");
       
        window.open("/homechatbot", "_blank");
    } else {
        alert("Usuario o contraseña incorrectos ✖️");
    }
});