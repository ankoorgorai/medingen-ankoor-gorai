import React from "react";
const ReviewCard = ({ review }) => (
  <div className="card">
    <h4>{review.reviewer}</h4>
    <p>{review.comment}</p>
  </div>
);
export default ReviewCard;
