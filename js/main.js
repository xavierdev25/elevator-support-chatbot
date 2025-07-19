// main.js
let flujoMantenimiento =
  JSON.parse(localStorage.getItem("flujoMantenimiento")) || null;

export async function getChatbotResponse(message) {
  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: message,
      mantenimiento_flujo: flujoMantenimiento,
    }),
    credentials: "omit", // Cambiado de 'include' a 'omit' para evitar problemas de CORS
  });
  const data = await res.json();
  if ("mantenimiento_flujo" in data) {
    flujoMantenimiento = data.mantenimiento_flujo;
    localStorage.setItem(
      "flujoMantenimiento",
      JSON.stringify(flujoMantenimiento)
    );
  }
  if (flujoMantenimiento === null || flujoMantenimiento === undefined) {
    flujoMantenimiento = null;
    localStorage.removeItem("flujoMantenimiento");
  }
  return data.response;
}
