
const batterySelect = document.getElementById("battery");
const analyzeButton = document.getElementById("analyze");
const message = document.getElementById("message");

analyzeButton.addEventListener("click", async () => {
  const batteryId = batterySelect.value;

  analyzeButton.disabled = true;
  message.textContent = `Checking available analysis for ${batteryId}...`;

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/dashboard?battery=${encodeURIComponent(batteryId)}`
    );

    if (!response.ok) {
      throw new Error("Backend returned an error.");
    }

    const result = await response.json();

    document.getElementById("health").textContent =
      result.health ?? "Not available";

    document.getElementById("rul").textContent =
      result.remaining_useful_life ?? "Not available";

    document.getElementById("anomaly").textContent =
      result.anomaly_status ?? "Not analyzed";

    document.getElementById("dataStatus").textContent =
      result.data_status ?? "Response received";

    message.textContent = result.message ?? "Request completed.";
  } catch (error) {
    message.textContent =
      "Backend is not running or is not reachable. Start the API and try again.";
    document.getElementById("dataStatus").textContent =
      "Backend disconnected";
  } finally {
    analyzeButton.disabled = false;
  }
});
