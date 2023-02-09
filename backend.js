const web3 = window.ethereum || new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

async function fetchData() {
  let data;
  if (window.ethereum) {
    await window.ethereum.enable();
    const accounts = await web3.eth.getAccounts();
    data = await web3.eth.getBlock(1, true);
  } else {
    // fetch data from backend
    const response = await fetch("/backend/data");
    data = await response.json();
  }
  console.log(data);
}

fetchData();
