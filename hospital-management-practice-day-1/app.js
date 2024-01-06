const loadProduct=(search)=>{
    fetch('https://fakestoreapi.com/products')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        displayProduct(data);
    })
}
const displayProduct=(products)=>{
    document.getElementById("product-card").innerHTML = "";
    products.forEach(product => {
        const parent=document.getElementById("product-card");
        const div = document.createElement("div");
        const truncatedDescription=product.description.length>150?product.description.substring(0,150)+'...':product.description
        div.innerHTML=`
        <div class="card mb-3" style="max-width: 540px;">
            <div class="row g-0">
            <div class="col-md-4">
                <img src="${product.image}" class="img-fluid rounded-start" alt="...">
            </div>
            <div class="col-md-8">
                <div class="card-body">
                <h5 class="card-title">${product.title}</h5>
                <p class="card-text">${truncatedDescription}</p>
                <p class="card-text">Category: ${product.category}</p>
                <button class="btn btn-primary">
                    <a target="_blank" href="productDetails.html?productId=${product.id}" class="text-dark">View</a>
                </button>
                </div>
            </div>
            </div>
        </div>
        `;
        parent.appendChild(div);
    });
}

const loadProductByCategory=(search)=>{
    console.log(search);
    fetch(`https://fakestoreapi.com/products/category/${search}`)
    .then(res => res.json())
    .then(data => displayProduct(data))
}

const loadCategories=()=>{
    fetch('https://fakestoreapi.com/products/categories')
    .then(res => res.json())
    .then(data =>{
        console.log(data);
        data.forEach(item =>{
            const parent = document.getElementById("category-drop");
            const li = document.createElement("li");
            const formattedSearch = item.replace(/\s/g, "%20");
            li.innerHTML=`
                <a class="dropdown-item" onclick="loadProductByCategory('${formattedSearch}')">${item}</a>
            `;
            parent.appendChild(li);
        })
    })
}

loadProduct();
loadCategories();