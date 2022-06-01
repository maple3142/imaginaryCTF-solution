const searchForm = document.getElementById("search-form");
const randomButton = document.getElementById("random-button");
const wordElement = document.getElementById("word-result");
const definitionElement = document.getElementById("definition-result");
const errorModal = document.getElementById("error-modal");
var errorMessage = "Unknown error";

function updateDefinition(word) {
  return fetch("/api/definition", {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ word: word }),
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      if (res.status === 404) {
        throw new Error(`No definition found for ${word}`);
      }
      throw new Error("Error getting definition");
    })
    .then((data) => {
      wordElement.textContent = data.word;
      definitionElement.textContent = data.definition;
    })
    .catch((err) => {
      errorMessage = err.message;
      const tempModal = new bootstrap.Modal(
        document.getElementById("error-modal")
      );
      tempModal.show();
    })
    .finally(() => {
      searchForm.elements["word"].value = "";
    });
}

function getRandom() {
  fetch("/api/random")
    .then((res) => res.json())
    .then((data) => updateDefinition(data.word))
    .catch((err) => console.error(err));
}

function searchWord(event) {
  event.preventDefault();
  const wordToSearch = searchForm.elements["word"].value || "flag";
  updateDefinition(wordToSearch);
}

function setModalMessage(event) {
  errorModal.querySelector("#modal-error-message").innerText = errorMessage;
}

searchForm.addEventListener("submit", searchWord);
randomButton.addEventListener("click", getRandom);
errorModal.addEventListener("show.bs.modal", setModalMessage);

getRandom();
