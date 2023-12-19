function Get_gift(table) {
  var userInput = document.getElementById("InputID").value;
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
function Add_gift() {
  const apiUrl = "http://127.0.0.1:8000/items/";
  var inputName = document.getElementById("InputName").value;
  try {
    var InputDescription = document.getElementById("InputDescription").value;
  } catch {
    var InputDescription = null;
  }
  var InputPrice = document.getElementById("InputPrice").value;
  try {
    var InputTax = document.getElementById("InputTax").value;
    //var InputTax = 0.0;
  } catch {
    var InputTax = 0.0;
  }
  data = {
    name: inputName,
    description: InputDescription,
    price: InputPrice,
    tax: InputTax,
  };
  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Specify the content type if sending JSON data
      // Add other headers if needed
    },
    body: JSON.stringify(data), // Convert data to JSON format
  })
    .then((response) => response.json()) // Parse the response as JSON
    .then((data) => console.log("Success:", data))
    .catch((error) => console.error("Error:", error));
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
  var headers = [
    "name",
    "description",
    "price",
    "tax",
    "price with tax",
    "item_id",
  ];
  for (let head in headers) {
    var headerCell = headerRow.insertCell();
    txt = headers[head];
    headerCell.textContent = txt;
  }
  container.appendChild(table);
  return table;
}
