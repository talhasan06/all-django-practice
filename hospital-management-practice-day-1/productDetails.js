const getParams=()=>{
    const param = new URLSearchParams(window.location.search).get("productId");
    console.log(param);
    fetch(`https://fakestoreapi.com/products/${param}`)
    .then(res => res.json())
    .then(data => displayDetails(data)) 
}
const displayDetails = (product) => {
    console.log(product);
    const parent = document.getElementById("product-details");
    const div = document.createElement("div");
    div.classList.add("product-details-container");
    div.innerHTML = `
    <div class="product-img">
        <img src=${product.image} alt="" />
        </div>
        <div class="doc-info">
        <h1>${product.title} </h1>
    
        <p class="w-50">
            ${product.description}
        </p>
    
        <h4>Price: ${product.price} USD</h4>
        <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
        >
        Buy Now
        </button>
    </div>`;
    parent.appendChild(div);
  };
  getParams();