const form = document.querySelector("#story-form");
const seed = document.querySelector("#seed");
const button = document.querySelector("#generate");
const status = document.querySelector("#status");
const story = document.querySelector("#story");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  button.disabled = true;
  story.hidden = true;
  status.textContent = "The house is listening…";

  try {
    const response = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ seed: seed.value }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "The story could not be generated.");
    story.textContent = data.story;
    story.hidden = false;
    status.textContent = "";
  } catch (error) {
    status.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});
