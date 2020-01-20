
import $ from 'jquery';

let form=document.getElementById('user-form');

form.addEventListener('submit',event=>{
    let user=form.elements['user']; //the name
    let avatarFile=form.elements['avatar-file'];

    let posting={
        user:user.value,
        avatarFile:avatarFile.value
    };

    let promise=$.post("http://5e20256ee31c6e0014c6031d.mockapi.io/api/v1/users",posting);
    promise.then(
        data=> console.log('success: ', data),
        error=> console.log('error: ', error)
    );
    
    let userError=document.getElementById('user-error');
    
    if(user.value.length < 4){
        userError.textContent='invalid entry';
        userError.style.color='red';
        userError.style.borderColor='red';
        user.focus();
    }
    console.log(user.value,avatarFile.value);
    event.preventDefault();
}); 