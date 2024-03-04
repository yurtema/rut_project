let blocksLoaded = 1; // Initial block loaded
const block5s = document.querySelectorAll('.block5'); // Select all block5 elements
const loadMoreBtn = document.getElementById('loadMore'); // Select the Load More button
const block4 = document.getElementById('block4'); // Select the block4 element

loadMoreBtn.addEventListener('click', loadMoreBlocks);

function loadMoreBlocks() {
    for (let i = 0; i < 4; i++) {
        const clone = block5s[0].cloneNode(true); // Clone the first block5 element
        block4.appendChild(clone); // Append the clone to block4
    }
    blocksLoaded += 1;
}
