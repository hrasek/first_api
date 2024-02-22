async function getAllGifts(table) {
  let i = 0;
  while (true) {
    try {
      gift = await getGift(i);
      if (gift) {
        displayData(gift, table);
        i++;
      } else {
        break;
      }
    } catch (error) {
      console.error(error);
      break;
    }
  }
}

async function getOneGift() {
  const id = document.getElementById("InputID").value;
  const gift = await getGift(id);
  if (gift) {
    displayData(gift, table);
  } else {
    alert("Dárek s tímto ID neexistuje");
  }
}

async function getGift(id) {
  const apiUrl = "http://127.0.0.1:8000/items/" + id.toString();

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    if (isObject(data)) {
      return data;
    } else {
      return null;
    }
  } catch (error) {
    console.error("Fetch error:", error);
    return null;
  }
}

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

async function addGift() {
  const apiUrl = "http://127.0.0.1:8000/items/";
  const inputName = document.getElementById("InputName").value;
  let InputDescription;
  try {
    InputDescription = document.getElementById("InputDescription").value;
  } catch {
    InputDescription = null;
  }
  const InputPrice = document.getElementById("InputPrice").value;
  let InputTax;
  if (document.getElementById("InputTax").value != "") {
    InputTax = document.getElementById("InputTax").value;
  } else {
    InputTax = null;
  }

  const data = {
    name: inputName,
    description: InputDescription,
    price: InputPrice,
    tax: InputTax,
  };

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const responseData = await response.json();
    console.log("Success:", responseData);
  } catch (error) {
    console.error("Error:", error);
  }
}

function displayData(data, table) {
  const dataContainer = document.getElementById("getGift_output");
  const values = Object.values(data);
  const row = table.insertRow();
  for (const value of values) {
    const cell = row.insertCell();
    cell.textContent = value;
  }
  dataContainer.appendChild(table);
}

function generateTableHeader() {
  const container = document.getElementById("tableHeader");
  const table = document.createElement("table");
  const headerRow = table.insertRow();
  const headers = ["Název", "Popis", "Cena", "Daň", "Cena s daní", "ID dárku"];
  for (const head in headers) {
    const headerCell = headerRow.insertCell();
    txt = headers[head];
    headerCell.textContent = txt;
  }
  container.appendChild(table);
  return table;
}
