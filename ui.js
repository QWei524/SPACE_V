var menuBtn = document.getElementById("menu-btn");
var dropdown = document.getElementById("dropdown");

menuBtn.addEventListener("click", function(e) {
    e.stopPropagation(); 
    if (dropdown.classList.contains("show")) {
        dropdown.classList.remove("show");
    } else {
        dropdown.classList.add("show");
    }
});


document.body.addEventListener("click", function(e) {
    if (e.target !== menuBtn && !dropdown.contains(e.target)) {
        dropdown.classList.remove("show");
    }
});

var WelcomePage = document.getElementById("Welcome-page");   
var LoginPage   = document.getElementById("Login-page");    
var SignupPage  = document.getElementById("Signup-page");   

var LoginBtn  = document.getElementById("Login-btn");
var SignupBtn = document.getElementById("Signup-btn");
var GuestBtn  = document.getElementById("Guest-btn");

var LoginBack  = document.getElementById("Login-back");
var SignupBack = document.getElementById("Signup-back");







loginBtn.addEventListener("click", function() {
    welcomePage.style.display = "none";
    loginPage.style.display = "flex";
    signupPage.style.display = "none";
    dropdown.classList.remove("show");
});

signupBtn.addEventListener("click", function() {
    welcomePage.style.display = "none";
    loginPage.style.display = "none";
    signupPage.style.display = "flex";
    dropdown.classList.remove("show");
});

if (guestBtn) {
    guestBtn.addEventListener("click", function() {
        alert("Guest mode. (TODO: 跳转主应用)");
    });
}

if (loginBack) {
    loginBack.addEventListener("click", function() {
        loginPage.style.display = "none";
        signupPage.style.display = "none";
        welcomePage.style.display = "flex";
    });
}

if (signupBack) {
    signupBack.addEventListener("click", function() {
        signupPage.style.display = "none";
        loginPage.style.display = "none";
        welcomePage.style.display = "flex";
    });
}

var loginSubmit = document.getElementById("login-submit");
if (loginSubmit) {
    loginSubmit.addEventListener("click", function() {
        var username = document.getElementById("login-username").value;
        var password = document.getElementById("login-password").value;
        if (username.length === 0 || password.length === 0) {
            alert("Please enter both username and password!");
        } else {
            alert("Login: " + username);
 
        }
    });
}

var signupSubmit = document.getElementById("signup-submit");
if (signupSubmit) {
    signupSubmit.addEventListener("click", function() {
        var username = document.getElementById("signup-username").value;
        var password = document.getElementById("signup-password").value;
        if (username.length === 0 || password.length === 0) {
            alert("Please enter both username and password!");
        } else {
            alert("Sign up: " + username);
        }
    });
}
