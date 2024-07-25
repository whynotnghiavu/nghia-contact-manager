// script.js
document.addEventListener("DOMContentLoaded", () => {
  const selectAllCheckbox = document.getElementById("selectAll");
  const rowCheckboxes = document.querySelectorAll(".selectRow");

  // Khi chọn tất cả
  selectAllCheckbox.addEventListener("change", (event) => {
    rowCheckboxes.forEach((checkbox) => {
      checkbox.checked = event.target.checked;
      checkbox.closest("tr").classList.toggle("selected", event.target.checked);
    });
  });

  // Khi chọn các hàng riêng lẻ
  rowCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      checkbox.closest("tr").classList.toggle("selected", checkbox.checked);

      // Cập nhật trạng thái của ô chọn tất cả
      const allChecked = Array.from(rowCheckboxes).every((cb) => cb.checked);
      selectAllCheckbox.checked = allChecked;
    });
  });
});

function editPhoneNumber(phone) {
  alert("Edit: " + phone);
}

function deletePhoneNumber(phone) {
  if (confirm("Bạn có chắc chắn muốn xóa số điện thoại này không?")) {
    fetch(`/delete/${phone}`, {
      method: "POST",
    //   headers: {
    //     "Content-Type": "application/x-www-form-urlencoded",
    //     "X-CSRFToken": "{{ csrf_token() }}", // Nếu bạn sử dụng CSRF protection
    //   },
    }).then((response) => {
      if (response.ok) {
        window.location.reload();
      } else {
        alert("Có lỗi xảy ra. Vui lòng thử lại.");
      }
    });
  }
}
