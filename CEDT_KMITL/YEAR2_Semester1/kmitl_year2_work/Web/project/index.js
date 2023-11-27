const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

sideLinks.forEach(link => {
    const li = item.parentElement;
        item.addEventListener('click', e => {
            e.preventDefault();
            sideLinks.forEach(link => link.classList.remove('active'));
            item.classList.add('active');
        });
});