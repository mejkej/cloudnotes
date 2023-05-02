const signInBtn = document.getElementById('tosigninbtn');
const signUpBtn = document.getElementById('tosignupbtn');
const signInForm = document.querySelector('.signinform');
const signUpForm = document.querySelector('.signupform');
const submitBtn = document.querySelector('.submitbtn');

signInBtn.addEventListener('click', (event) => {
    event.preventDefault();
signInForm.style.display = 'block';
signUpForm.style.display = 'none';
});

signUpBtn.addEventListener('click', (event) => {
    event.preventDefault();
    signUpForm.style.display = 'block';
    signInForm.style.display = 'none';
    });

document.querySelector('.signinform .submitbtn').addEventListener('click', function(event) {   
    if () {
        document.getElementById('signinerror').textContent = 'Custom error message for sign in form';
        event.preventDefault();
    }
});

document.querySelector('.signupform .submitbtn').addEventListener('click', function(event) {   
    if () {
        document.getElementById('signuperror').textContent = 'Custom error message for sign up form';
        event.preventDefault();
    }
});














