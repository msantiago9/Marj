let size = document.getElementsByClassName("stackedit__html");

const toggleSize = () => {
  size[0].classList.toggle("normal");
  size[0].classList.toggle("zoom");
  fetch("/size", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      size: size[0].classList.contains("normal") ? "normal" : "zoom",
    }),
  });
};
