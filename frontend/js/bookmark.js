import { getBookmarks, createBookmark, updateBookmark, deleteBookmark } from "./api.js";

const bookmarkForm = document.getElementById("bookmark-form");
const bookmarkTableBody = document.querySelector("#bookmark-list tbody");

// Affichage
async function renderBookmarks() {
    const bookmarks = await getBookmarks();
    bookmarkTableBody.innerHTML = "";

    bookmarks.forEach(bm => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${bm.title}</td>
            <td><a href="${bm.url}" target="_blank">${bm.url}</a></td>
            <td>${bm.description || ""}</td>
            <td>
                <button class="edit-btn" data-id="${bm.id}">✏️</button>
                <button class="delete-btn" data-id="${bm.id}">🗑️</button>
            </td>
        `;

        bookmarkTableBody.appendChild(tr);
    });
}

// Gestion des clics (Event Delegation)
bookmarkTableBody.addEventListener("click", async (e) => {
    const button = e.target.closest("button");
    if (!button) return;

    const id = button.dataset.id;

    // DELETE
    if (button.classList.contains("delete-btn")) {
        if (confirm("Supprimer ce bookmark ?")) {
            await deleteBookmark(id);
            renderBookmarks();
        }
    }

    // UPDATE
    if (button.classList.contains("edit-btn")) {
        const currentRow = button.closest("tr");

        const currentTitle = currentRow.children[0].innerText;
        const currentUrl = currentRow.children[1].querySelector("a").href; // ⚡ corrige la récupération de l'URL
        const currentDesc = currentRow.children[2].innerText;

        const title = prompt("Nouveau titre:", currentTitle);
        const url = prompt("Nouvelle URL:", currentUrl);
        const description = prompt("Nouvelle description:", currentDesc);

        if (!title || !url) {
            alert("Titre et URL obligatoires");
            return;
        }

        console.log("UPDATE FRONT:", { id, title, url, description });
        await updateBookmark(id, { title, url, description });

        renderBookmarks();
    }
});

// FORM
bookmarkForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const title = document.getElementById("bm-title").value;
    const url = document.getElementById("bm-url").value;
    const description = document.getElementById("bm-desc").value;

    await createBookmark({ title, url, description });

    bookmarkForm.reset();
    renderBookmarks();
});

// START
renderBookmarks();