// document.addEventListener("DOMContentLoaded", () => {
//   const selectAllCheckbox = document.getElementById("selectAll");
//   const rowCheckboxes = document.querySelectorAll(".selectRow");

//   selectAllCheckbox.addEventListener("change", (event) => {
//     rowCheckboxes.forEach((checkbox) => {
//       checkbox.checked = event.target.checked;
//       checkbox.closest("tr").classList.toggle("selected", event.target.checked);
//     });
//   });

//   rowCheckboxes.forEach((checkbox) => {
//     checkbox.addEventListener("change", () => {
//       checkbox.closest("tr").classList.toggle("selected", checkbox.checked);

//       const allChecked = Array.from(rowCheckboxes).every((cb) => cb.checked);
//       selectAllCheckbox.checked = allChecked;
//     });
//   });
// });

function editPhoneNumber(phone) {
  alert("Chưa phát triển: " + phone);
}

function deletePhoneNumber(phone, name, file) {
  if (confirm("Bạn có chắc chắn muốn xóa số điện thoại này không?")) {
    fetch(`/delete/${phone}/${name}/${file}`, {
      method: "POST",
    }).then((response) => {
      if (response.ok) {
        window.location.reload();
      } else {
        alert("Có lỗi xảy ra. Vui lòng thử lại.");
      }
    });
  }
}
