function Get_gift(table) {
  var userInput = document.getElementById("userInput").value;
  const apiUrl = "http://127.0.0.1:8000/items/" + userInput.toString();

  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      displayData(data, table);
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

function displayData(data, table) {
  const dataContainer = document.getElementById("Get_gift_output");
  var values = Object.values(data);
  //  let txt = "";
  // var table = document.createElement("table");
  var row = table.insertRow();
  for (let value of values) {
    txt = value;
    var cell = row.insertCell();
    cell.textContent = txt;
  }
  dataContainer.appendChild(table);
}

function generateTableHeader() {
  var container = document.getElementById("tableHeader");
  var table = document.createElement("table");
  var headerRow = table.insertRow();
  // var keys = Object.keys(data);
  var headers = ["name", "description", "price", "tax", "item_id"];
  for (let head in headers) {
    var headerCell = headerRow.insertCell();
    txt = headers[head];
    headerCell.textContent = txt;
  }
  container.appendChild(table);
  return table;
}
