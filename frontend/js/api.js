// Remplace par l'IP réelle où tourne Flask
const API_URL = "http://10.76.30.145:5000/bookmarks/";

// GET
export async function getBookmarks() {
    try {
        const res = await fetch(API_URL);
        if (!res.ok) throw new Error("Erreur GET");
        return await res.json();
    } catch (err) {
        console.error("GET ERROR:", err);
        return [];
    }
}

// POST
export async function createBookmark(bookmark) {
    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bookmark)
        });
        if (!res.ok) throw new Error("Erreur POST");
        return await res.json();
    } catch (err) {
        console.error("POST ERROR:", err);
    }
}

// PUT
export async function updateBookmark(id, bookmark) {
    try {
        const url = `${API_URL}${id}`;
        console.log("PUT URL:", url, "BODY:", bookmark);

        const res = await fetch(url, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bookmark)
        });

        if (!res.ok) throw new Error("Erreur PUT");
        return await res.json();
    } catch (err) {
        console.error("PUT ERROR:", err);
    }
}

// DELETE
export async function deleteBookmark(id) {
    try {
        const url = `${API_URL}${id}`;
        console.log("DELETE URL:", url);

        const res = await fetch(url, {
            method: "DELETE"
        });

        if (!res.ok) throw new Error("Erreur DELETE");
        return await res.json();
    } catch (err) {
        console.error("DELETE ERROR:", err);
    }
}