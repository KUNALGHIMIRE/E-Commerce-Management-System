function Navbar({ cartCount }) {
  return (
    <nav className="p-4 bg-gray-800 text-white flex justify-between">
      <h1 className="font-bold text-xl">MyStore</h1>
      <div>Cart: {cartCount}</div>
    </nav>
  );
}
export default Navbar;
