let light = document.querySelector("link[href='/static/light.css']") !== null;
const toggleTheme = () => {
  if (light) {
    document.querySelector("link[href='/static/light.css']").href =
      "/static/dark.css";
  } else {
    document.querySelector("link[href='/static/dark.css']").href =
      "/static/light.css";
  }
  light = !light;
  fetch("/theme", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      theme: light ? "light" : "dark",
    }),
  });
};
