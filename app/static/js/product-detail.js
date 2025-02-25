function initProductDetail() {
  // Get references to the elements
  const quantityInput = document.getElementById("quantity_count");
  const incrementBtn = document.getElementById("increment-btn");
  const decrementBtn = document.getElementById("decrement-btn");
  const addToCartBtn = document.getElementById("add-to-cart-btn");

  // Add event listeners with inline functions for clarity
  incrementBtn.addEventListener("click", function () {
    let currentValue = parseInt(quantityInput.value) || 1;
    quantityInput.value = currentValue + 1;
  });

  decrementBtn.addEventListener("click", function () {
    let currentValue = parseInt(quantityInput.value) || 1;
    if (currentValue > 1) {
      quantityInput.value = currentValue - 1;
    }
  });

  addToCartBtn.addEventListener("click", function () {
    let quantity = parseInt(quantityInput.value) || 1;
    console.log("Adding to cart:", productId, "quantity:", quantity);
  });

  // Prevent form submission if quantity buttons are inside a form
  quantityInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
    }
  });

  // Validate input to ensure it's a positive number
  quantityInput.addEventListener("change", function () {
    let value = parseInt(this.value) || 1;
    if (value < 1) value = 1;
    this.value = value;
  });
}

document.addEventListener("DOMContentLoaded", initProductDetail);
