// script.js
document.addEventListener('DOMContentLoaded', () => {
    const selectAllCheckbox = document.getElementById('selectAll');
    const rowCheckboxes = document.querySelectorAll('.selectRow');

    // Khi chọn tất cả
    selectAllCheckbox.addEventListener('change', (event) => {
        rowCheckboxes.forEach(checkbox => {
            checkbox.checked = event.target.checked;
            checkbox.closest('tr').classList.toggle('selected', event.target.checked);
        });
    });

    // Khi chọn các hàng riêng lẻ
    rowCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            checkbox.closest('tr').classList.toggle('selected', checkbox.checked);
            
            // Cập nhật trạng thái của ô chọn tất cả
            const allChecked = Array.from(rowCheckboxes).every(cb => cb.checked);
            selectAllCheckbox.checked = allChecked;
        });
    });
});



function editPhoneNumber(PhoneNumber) {
  alert("Edit: " + PhoneNumber);
}
function deletePhoneNumber(PhoneNumber) {
  alert("Delete: " + PhoneNumber);
}