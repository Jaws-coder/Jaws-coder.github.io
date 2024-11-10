document.getElementById("signin").addEventListener("click", function () {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username && password) {
    // Handle the form submission here
    console.log("Username:", username);
    console.log("Password:", password);
  } else {
    alert("Please fill in both fields.");
  }
});

