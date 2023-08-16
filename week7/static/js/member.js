document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");

  deleteButtons.forEach((button) => {
    const userId = button.dataset.userId;
    button.addEventListener("click", function () {
      const messageId = button.dataset.messageId;
      confirmDelete(messageId, userId);
    });
  });
});

function confirmDelete(messageId) {
  console.log("Deleting message with ID:", messageId);
  const confirmResult = confirm("確定要刪除留言嗎？");

  if (confirmResult) {
    fetch(`/deleteMessage?message_id=${messageId}`, {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          location.reload();
        } else {
          alert("刪除操作失敗，請稍後再試。");
        }
      });
  }
}
document.addEventListener("DOMContentLoaded", function () {
  const queryButton = document.getElementById("query-button");
  const resultDiv = document.getElementById("result");

  queryButton.addEventListener("click", function () {
    const username = document.getElementById("query-username").value;

    fetch(`/api/member?username=${username}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.data) {
          resultDiv.textContent = `${data.data.name}(${data.data.username})`;
        } else {
          resultDiv.textContent = "無此會員";
        }
      })
      .catch((error) => {
        console.error("發生錯誤：", error);
        resultDiv.textContent = "查詢過程中發生錯誤";
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const updateNameButton = document.getElementById("update-name-button");
  const newNameInput = document.getElementById("new-name");
  const updateNameResult = document.getElementById("update-name-result");
  const renewName = document.getElementById("renew_name");

  updateNameButton.addEventListener("click", function () {
    const newName = newNameInput.value;

    fetch("/api/member", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: newName }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.ok) {
          updateNameResult.textContent = "更新成功";
          renewName.textContent = `${newName}，您已成功登入系統`;
        } else {
          updateNameResult.textContent = "姓名更新失敗";
        }
      })
      .catch((error) => {
        console.error("發生錯誤：", error);
        updateNameResult.textContent = "姓名更新過程中發生錯誤";
      });
  });
});
