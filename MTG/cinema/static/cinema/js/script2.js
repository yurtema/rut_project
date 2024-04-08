document.addEventListener('DOMContentLoaded', function() {
    let loadButton = document.createElement('button');
    loadButton.textContent = 'Загрузить еще';
    loadButton.classList.add('load-button');
    document.body.appendChild(loadButton);
    
    loadButton.addEventListener('click', function() {
        let blocksToLoad = document.querySelectorAll('.block5');

        for (let i = 0; i < 4; i++) {
            let block = blocksToLoad[number];
            if (block) {
                block.style.display = 'block';
            } else {
                loadButton.style.display = 'none';
                break;
            }
            number++;
        }
    });
});
