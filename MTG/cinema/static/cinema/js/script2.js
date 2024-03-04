let currentIndex = 0;
const block5Elements = document.querySelectorAll('.block5');
const showNextButton = document.getElementById('showNext');

function showNextFour() {
    const nextIndex = currentIndex + 4;
    for (let i = currentIndex; i < nextIndex; i++) {
        if (block5Elements[i]) {
            block5Elements[i].style.display = 'block';
        }
    }
    currentIndex = nextIndex;
}

showNextFour(); // Show the initial 4 block5 elements

showNextButton.addEventListener('click', showNextFour);
