function ProductModal({ product, onClose }) {
  if (!product) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded shadow-lg w-96 relative">
        <button onClick={onClose} className="absolute top-2 right-2 text-red-500">X</button>
        <img src={product.image} alt={product.name} className="w-full h-40 object-cover"/>
        <h2 className="font-bold text-xl mt-2">{product.name}</h2>
        <p className="mt-2">{product.description}</p>
        <p className="mt-2 font-bold">${product.price}</p>
      </div>
    </div>
  );
}
export default ProductModal;
