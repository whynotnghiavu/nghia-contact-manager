// script.js
document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('myTable');

    table.addEventListener('click', (event) => {
        const target = event.target;
        if (target.tagName === 'TD') {
            const row = target.parentNode;
            const previouslySelected = table.querySelector('tr.selected');
            if (previouslySelected) {
                previouslySelected.classList.remove('selected');
            }
            row.classList.add('selected');
        }
    });
});
