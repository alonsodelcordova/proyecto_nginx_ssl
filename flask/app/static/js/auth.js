

document.getElementById('authForm')?.addEventListener('submit', async function (e) {
    e.preventDefault();
    const responseDiv = document.getElementById('response');

    const form = e.target;
    const email = form.email.value;
    const password = form.password.value;

    const data = { email, password };

    const endpoint = '/login';

    const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await res.json();

    if (res.ok) {
        responseDiv.innerHTML = `<div class="alert alert-success">Inicio de sesión exitoso</div>`;
        if (result.token) {
            localStorage.setItem('token', result.token); // almacena token
            window.location.href = '/admin';
        }
    } else {
        responseDiv.innerHTML = `<div class="alert alert-danger">${result.message || 'Error'}</div>`;
    }
});




document.getElementById('registerForm')?.addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;
    const email = form.email.value;
    const password = form.password.value;
    const password2 = form.password2.value;
    const name = form.name.value;
    const responseDiv = document.getElementById('response');

    if (password !== password2) {
        responseDiv.innerHTML = `<div class="alert alert-danger">Las contraseñas no coinciden</div>`;
        return;
    }

    const data = { email, password, name };
    const endpoint =  '/register' ;

    const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await res.json();   

    if (res.ok) {
        responseDiv.innerHTML = `<div class="alert alert-success">Usuario registrado</div>`;
        // sleep(1000);
        setTimeout(() => {
            window.location.href = '/';
        }, 1000);
    } else {
        responseDiv.innerHTML = `<div class="alert alert-danger">${result.message || 'Error'}</div>`;
    }
});