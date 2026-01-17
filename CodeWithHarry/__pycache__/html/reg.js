const regform=document.getElementById('regform');
const errmsg=document.getElementById('errmsg1');
const errmsgg=document.getElementById('errmsg2');
const errmsggg=document.getElementById('errmsg3');
regform.addEventListener('submit', function (event) {
    event.preventDefault();
    //console.log(regForm.elements);
    const{username,password,email} = regform.nextElementSibling;
   
    if (username.value.trim().length === 0) {
        errmsg.innerHTML = 'Please enter username';
        return;
    }

    if (!isValidEmail(email.value)) {
        errmsgg.innerHTML = 'Please enter correct email';
        //alert('Please enter correct email')
        return;
    }
    function isValidEmail() {
        const exp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        console.log(exp.test(email.value));
    }
});



