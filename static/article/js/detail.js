console.log("go");

window.addEventListener("load", () => {
  color = "red";
  if (Number(liked)) color = "blue";
  document.querySelector("#like").style.backgroundColor = color;
});

document.querySelector("#like").addEventListener("click", async (event) => {
  const response = await fetch(`${likeUrl}?user=${userId}`).then((res) =>
    res.json()
  );
  console.log(response);
  if (response.message === "created") {
    event.target.style.backgroundColor = "blue";
  } else {
    event.target.style.backgroundColor = "red";
  }
  event.target.textContent = `♥ ${response.count}`;
});
