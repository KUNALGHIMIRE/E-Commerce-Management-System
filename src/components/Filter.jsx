function Filter({ categories, selectedCategory, onSelectCategory }) {
  return (
    <div className="filter">
      {categories.map((cat) => (
        <button
          key={cat}
          className={selectedCategory === cat ? "active" : ""}
          onClick={() => onSelectCategory(cat)}
        >
          {cat}
        </button>
      ))}
    </div>
  );
}

export default Filter;
