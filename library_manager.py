import streamlit as st

class PersonalLibraryManager:
    def __init__(self):
        if "books" not in st.session_state:
            st.session_state.books = []  # Initialize book storage
        if "new_books" not in st.session_state:
            st.session_state.new_books = []  # Temporary storage for multiple books

    def add_books(self, books):
        """Add multiple books at once."""
        st.session_state.books.extend(books)
        st.session_state.new_books = []  # Clear the temporary book list
        return f"✅ {len(books)} books added successfully!"

    def remove_book(self, title):
        """Remove a book by title."""
        for book in st.session_state.books:
            if book["title"].lower() == title.lower():
                st.session_state.books.remove(book)
                return f"🗑️ Book '{title}' removed."
        return f"⚠️ Book '{title}' not found."

    def search_books(self, query, key):
        """Search books by title or author."""
        return [book for book in st.session_state.books if query.lower() in book[key].lower()]

    def display_statistics(self):
        """Calculate and return library statistics."""
        total_books = len(st.session_state.books)
        read_books = sum(1 for book in st.session_state.books if book["read_status"])
        unread_books = total_books - read_books

        # Avoid division by zero
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

        return total_books, read_books, unread_books, percentage_read

# Initialize Library Manager
manager = PersonalLibraryManager()

def add_multiple_books_ui():
    """UI for adding multiple books."""
    st.subheader("➕ Add Multiple Books")

    # Add a new book input row
    if st.button("➕ Add Another Book"):
        st.session_state.new_books.append({"title": "", "author": "", "year": 0, "genre": "", "read_status": False})

    # Display dynamic book input fields
    for idx, book in enumerate(st.session_state.new_books):
        st.markdown(f"### 📖 Book {idx + 1}")
        book["title"] = st.text_input(f"Title {idx+1}", value=book["title"], key=f"title_{idx}")
        book["author"] = st.text_input(f"Author {idx+1}", value=book["author"], key=f"author_{idx}")
        book["year"] = st.number_input(f"Year {idx+1}", min_value=0, step=1, value=book["year"], key=f"year_{idx}")
        book["genre"] = st.text_input(f"Genre {idx+1}", value=book["genre"], key=f"genre_{idx}")
        book["read_status"] = st.checkbox(f"Read {idx+1}", value=book["read_status"], key=f"read_{idx}")

    # Submit all books at once
    if st.button("✅ Add All Books"):
        if all(book["title"] and book["author"] and book["year"] and book["genre"] for book in st.session_state.new_books):
            message = manager.add_books(st.session_state.new_books)
            st.success(message)
        else:
            st.error("⚠️ Please fill in all fields for all books.")

# Sidebar menu
st.title("📚 Personal Library Manager")
menu = st.sidebar.radio("📌 Menu", ["Add Multiple Books", "Remove Book", "Search Books", "Display All Books", "Statistics"])

# Add Multiple Books UI
if menu == "Add Multiple Books":
    add_multiple_books_ui()

# Remove Book Section
elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    title = st.text_input("📖 Enter the title of the book to remove")
    
    if st.button("Remove Book"):
        message = manager.remove_book(title)
        st.success(message)

# Search Books Section
elif menu == "Search Books":
    st.subheader("🔎 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("🔍 Enter your search query")

    if st.button("Search"):
        key = "title" if search_by == "Title" else "author"
        results = manager.search_books(query, key)

        if results:
            st.write(f"### 📚 Search Results ({len(results)} found):")
            for book in results:
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read_status'] else '❌ Unread'}")
        else:
            st.warning("⚠️ No matching books found.")

# Display All Books Section
elif menu == "Display All Books":
    st.subheader("📚 Your Library Collection")
    if st.session_state.books:
        for book in st.session_state.books:
            st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read_status'] else '❌ Unread'}")
    else:
        st.info("ℹ️ No books in your library yet. Start adding some!")

# Statistics Section
elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books, read_books, unread_books, percentage_read = manager.display_statistics()
    
    st.write(f"📚 **Total books:** {total_books}")
    st.write(f"✅ **Read books:** {read_books}")
    st.write(f"❌ **Unread books:** {unread_books}")
    st.write(f"📖 **Percentage read:** {percentage_read:.1f}%")
