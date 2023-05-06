const buttons = document.querySelectorAll('.circle-blue','circle-green','circle-orange');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active');
    });
});

