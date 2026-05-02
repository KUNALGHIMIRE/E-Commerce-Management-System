function ProductCard({ product, onAddToCart, onViewDetails }) {
  return (
    <div className="border p-4 rounded shadow hover:shadow-lg">
      <img src={product.image} alt={product.name} className="w-full h-40 object-cover"/>
      <h2 className="font-bold mt-2">{product.name}</h2>
      <p>${product.price}</p>
      <div className="mt-2 flex gap-2">
        <button
          className="bg-green-500 text-white px-2 py-1 rounded"
          onClick={() => onAddToCart(product)}
        >
          Add to Cart
        </button>
        <button
          className="bg-blue-500 text-white px-2 py-1 rounded"
          onClick={() => onViewDetails(product)}
        >
          View
        </button>
      </div>
    </div>
  );
}
export default ProductCard;
