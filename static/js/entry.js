const signInBtn = document.getElementById('signinbtn');
const signUpBtn = document.getElementById('signupbtn');
const signInForm = document.getElementById('signinform');
const signUpForm = document.getElementById('signupform');
const signInSubmit = document.getElementById('submitsigninbtn');
const signUpSubmit = document.getElementById('submitsignupbtn');

signInBtn.addEventListener('click', () => {
    signInForm.classList.remove('hidden');
})

signUpBtn.addEventListener('click', () => {
    signUpForm.classList.remove('hidden');
})



