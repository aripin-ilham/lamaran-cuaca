const btn = document.getElementById('theme-switch');
btn.onclick = () => {
    document.body.classList.toggle('dark-mode');
    localStorage.theme = document.body.classList.contains('dark-mode');
};
if (localStorage.theme === 'true') document.body.classList.add('dark-mode');