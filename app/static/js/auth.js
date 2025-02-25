function checkAuthState() {
  const token = localStorage.getItem("token");
  const userFirstName = localStorage.getItem("userFirstName");
  const loginButton = document.getElementById("loginButton");
  const userDropdown = document.getElementById("userDropdown");
  const userFirstNameSpan = document.getElementById("userFirstName");

  if (token && userFirstName) {
    loginButton.classList.add("d-none");
    userDropdown.classList.remove("d-none");
    userFirstNameSpan.textContent = userFirstName;
  } else {
    loginButton.classList.remove("d-none");
    userDropdown.classList.add("d-none");
    userFirstNameSpan.textContent = "";
  }
}

async function handleLogout() {
  localStorage.removeItem("token");
  localStorage.removeItem("userFirstName");
  checkAuthState();
  window.location.reload();
}

async function handleLogin() {
  const form = document.getElementById("login-form");
  const formData = new FormData(form);
  const data = {
    email: formData.get("email"),
    password: formData.get("password"),
  };

  console.log("Login attempt with:", data);

  try {
    const response = await fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    console.log("Response status:", response.status);
    const result = await response.json();
    console.log("Response data:", result);

    if (response.ok) {
      localStorage.setItem("token", result.access_token);
      localStorage.setItem("userFirstName", result.first_name); // Add this line
      $("#modallogin").modal("hide");
      window.location.reload();
    } else {
      alert(result.detail || "Login failed");
    }
  } catch (error) {
    console.error("Login error:", error);
    alert("An error occurred during login");
  }
}

async function handleRegister() {
  const form = document.getElementById("register-form");
  const formData = new FormData(form);
  const data = {
    first_name: formData.get("first_name"),
    last_name: formData.get("last_name"),
    email: formData.get("email"),
    password: formData.get("password"),
  };

  try {
    const response = await fetch("/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (response.ok) {
      alert("Registration successful! Please login.");
      $("#modalregister").modal("hide");
      $("#modallogin").modal("show");
    } else {
      alert(result.detail);
    }
  } catch (error) {
    alert("An error occurred during registration");
  }
}

// Add this to initialize the auth state
document.addEventListener("DOMContentLoaded", checkAuthState);
