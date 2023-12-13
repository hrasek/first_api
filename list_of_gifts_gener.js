function Get_gift() {
  const apiUrl = "http://127.0.0.1:8000/items/0";

  // Using the fetch function to make a GET request
  fetch(apiUrl)
    .then((response) => {
      // Check if the response status is OK (status code 200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the JSON content of the response
      return response.json();
    })
    .then((data) => {
      // Handle the data from the local API
      console.log(data);
    })
    .catch((error) => {
      // Handle errors that may occur during the fetch
      console.error("Fetch error:", error);
    });
}
// function Bezlepku() {
//   document.getElementById("bezlepkuOutput").innerHTML =
//     "Zeleninový krém <br> Svíčková na smetaně s bezlepkovým karlovarským knedlíkem, šlehačkou a brusinkami ";
// }
// function Vege() {
//   document.getElementById("vegeOutput").innerHTML =
//     "Zeleninový krém <br> Falafel s bramborem, zeleninová obloha ";
// }
