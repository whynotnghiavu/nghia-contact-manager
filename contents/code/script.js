document.addEventListener('DOMContentLoaded', function() {
    const toggleDarkModeCheckbox = document.getElementById('toggle-dark-mode');

    toggleDarkModeCheckbox.addEventListener('change', function() {
        document.body.classList.toggle('dark-mode');
    });

    // Persist Dark Mode setting using localStorage
    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('dark-mode');
        toggleDarkModeCheckbox.checked = true;
    }

    toggleDarkModeCheckbox.addEventListener('change', function() {
        if (toggleDarkModeCheckbox.checked) {
            document.body.classList.add('dark-mode');
            localStorage.setItem('dark-mode', 'enabled');
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('dark-mode', 'disabled');
        }
    });
});
