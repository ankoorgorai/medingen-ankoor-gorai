import React from "react";

const ProductCard = ({ product }) => (
  <div className="card">
    <h3>{product.name}</h3>
    <p>{product.description}</p>
    <p>Salt content: {product.salt_content} mg</p>
    <p>Price: ₹{product.price}</p>
  </div>
);

export default ProductCard;
