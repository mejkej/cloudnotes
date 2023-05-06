const signInBtn = document.getElementById('tosigninbtn');
const signUpBtn = document.getElementById('tosignupbtn');
const signInForm = document.querySelector('.signinform');
const signUpForm = document.querySelector('.signupform');

signInBtn.addEventListener('click', (event) => {
    event.preventDefault();
    signInForm.style.display = 'block';
    signUpForm.style.display = 'none';
    }
);

signUpBtn.addEventListener('click', (event) => {
    event.preventDefault();
    signUpForm.style.display = 'block';
    signInForm.style.display = 'none';
    }
);















