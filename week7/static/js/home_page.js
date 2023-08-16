const signup = document.getElementById("signup");
signup.addEventListener("submit", function (event) {
  const name = document.getElementById("name");
  const username = document.getElementById("username");
  const password = document.getElementById("password");

  if (!name.value || !username.value || !password.value) {
    event.preventDefault();
    alert("請輸入完整資訊");
  }
});

const loginForm = document.getElementById("login");

loginForm.addEventListener("submit", function (event) {
  const usernameInput = document.getElementById("signname");
  const passwordInput = document.getElementById("signpassword");

  if (!usernameInput.value || !passwordInput.value) {
    event.preventDefault();
    alert("請輸入帳號或密碼");
  }
});
