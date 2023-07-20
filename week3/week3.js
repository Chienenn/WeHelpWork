let menuIcon = document.getElementById("menu-icon");
let mobileNav = document.querySelector(".mobile-nav");

menuIcon.addEventListener("click", function () {
  mobileNav.classList.toggle("show");
});

document.addEventListener("DOMContentLoaded", () => {
  fetchAttractions();
});

async function fetchAttractions() {
  try {
    const response = await fetch(
      "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    );
    const data = await response.json();
    const attractions = data.result.results;

    const colElements = document.querySelectorAll(".col");
    const promotionElements = document.querySelectorAll(".promotion");
    const promotion3Element = document.querySelector(".promotion3");
    for (let i = 0; i < promotionElements.length && i < 3; i++) {
      const stitle = attractions[i].stitle;
      const boxTextElement = promotionElements[i].querySelector(".box-text");
      boxTextElement.textContent = stitle;
      const imageUrl = getFirstImageUrl(attractions[i].file);
      if (imageUrl) {
        const imageElement = document.createElement("img");
        imageElement.src = imageUrl;
        promotionElements[i].querySelector(".box-image").src = imageUrl;
      }
    }
    const stitlePromotion3 = attractions[2].stitle;
    const boxTextElementPromotion3 =
      promotion3Element.querySelector(".box-text");
    boxTextElementPromotion3.textContent = stitlePromotion3;
    const imageUrlPromotion3 = getFirstImageUrl(attractions[2].file);
    if (imageUrlPromotion3) {
      promotion3Element.querySelector(".box-image").src = imageUrlPromotion3;
    }

    for (let i = 0; i < colElements.length && i < attractions.length; i++) {
      const colElement = colElements[i];
      const stitle = attractions[i + 3].stitle;
      const imageUrl = getFirstImageUrl(attractions[i + 3].file);

      while (colElement.firstChild) {
        colElement.removeChild(colElement.firstChild);
      }

      if (imageUrl) {
        const imageElement = document.createElement("img");
        imageElement.src = imageUrl;
        imageElement.alt = stitle;
        imageElement.className = "image";
        colElement.appendChild(imageElement);
      }

      const picTxtElement = document.createElement("div");
      picTxtElement.className = "pic-txt";
      picTxtElement.textContent = stitle;
      colElement.appendChild(picTxtElement);
    }
  } catch (error) {
    console.error("Error fetching attractions:", error);
  }
}

function getFirstImageUrl(file) {
  const pattern = /https:\/\/[\w./-]+\.(jpg|JPG)/;
  const matches = file.match(pattern);
  return matches ? matches[0] : null;
}
